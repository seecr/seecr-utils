## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2013-2014, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
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
        debugprompt = DebugPrompt(reactor=reactor, port=9999, globals={'reactor': reactor})
        dna = be((Observable(),
            (debugprompt,)
        ))
        list(compose(dna.once.observer_init()))
        def runServer():
            while not stopped:
                reactor.step()
        t = Thread(target=runServer)
        t.start()

        try:
            with socket() as sok:
                sok.connect(('localhost', 9999))
                self.assertEqual(b"Debug >> ", sok.recv(1024))
                sok.send(b'a=5')
                self.assertEqual(b"Debug >> ", sok.recv(1024))
                sok.send(b"print(a)")
                self.assertEqual(b"5\nDebug >> ", sok.recv(1024))
                sok.send(b"syntax error")

                response = sok.recv(2024).decode()
                self.assertEqualsWS("""File "<string>", line 1
        syntax error
               ^^^^^
    SyntaxError: invalid syntax
    Debug >> """, response)

                sok.sendall(b"print(dir())")
                self.assertEqual(b"['__builtins__', 'a', 'reactor']\nDebug >> ", sok.recv(8192))

            with socket() as sok:
                sok.connect(('localhost', 9999))
                self.assertEqual(b"Debug >> ", sok.recv(1024))
                sok.send(b"print(a)")
                self.assertEqual(b"5\nDebug >> ", sok.recv(1024))
        finally:
            stopped.append(True)
            t.join()
            debugprompt.close()

