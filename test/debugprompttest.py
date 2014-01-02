## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2013 Seecr (Seek You Too B.V.) http://seecr.nl
#
# This file is part of "Seecr Utils"
#
# "Seecr Utils" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Seecr Utils" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr Utils"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from weightless.core import be, compose
from weightless.io import Reactor
from meresco.core import Observable
from seecr.utils import DebugPrompt

from seecr.test import SeecrTestCase

from socket import socket
from threading import Thread

from sys import version_info
python26 = version_info[0:2] == (2, 6)

class DebugPromptTest(SeecrTestCase):

    def testOne(self):
        stopped = []
        reactor = Reactor()
        dna = be((Observable(),
            (DebugPrompt(reactor=reactor, port=9999, globals={'reactor': reactor}),),
        ))
        list(compose(dna.once.observer_init()))
        def runServer():
            while not stopped:
                reactor.step()
        t = Thread(target=runServer)
        t.start()

        try:
            sok = socket()
            sok.connect(('localhost', 9999))
            self.assertEqual(b"Debug >> ", sok.recv(1024))
            sok.send(b'a=5')
            self.assertEqual(b"Debug >> ", sok.recv(1024))
            sok.send(b"print (a)")
            self.assertEqual(b"5\nDebug >> ", sok.recv(1024))
            sok.send(b"syntax error")
            self.assertEqual(b'Traceback (most recent call last):\n  File "<string>", line 1\n    syntax error\n               ^\nSyntaxError: invalid syntax\nDebug >> ', sok.recv(1024))
            sok.sendall(b"print (dir()) ")
            self.assertEqual(b"['__builtins__', 'a', 'reactor']\nDebug >> ", sok.recv(8192))
            sok.close()

            sok = socket()
            sok.connect(('localhost', 9999))
            self.assertEqual(b"Debug >> ", sok.recv(1024))
            sok.send(b"print (a)")
            self.assertEqual(b"5\nDebug >> ", sok.recv(1024))
            sok.close()
        finally:
            stopped.append(True)

