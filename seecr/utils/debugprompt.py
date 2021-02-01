## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2013, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
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

from weightless.http import Acceptor
from io import StringIO
from traceback import print_exc
import sys
from weightless.core import identify

PROMPT = b"Debug >> "

class DebugPrompt(object):

    def __init__(self, reactor, port, globals):
        self._reactor = reactor
        self._port = port
        self._globals = globals

    def observer_init(self):
        self._acceptor = Acceptor(
            reactor=self._reactor,
            port=self._port,
            sinkFactory=self._connect,
            bindAddress='127.0.0.1')

    def _connect(self, sok):
        next(self.handle_conversation(sok))

    def close(self):
        self._acceptor.close()

    @identify
    def handle_conversation(self, sok):
        response = PROMPT
        this  = yield
        while True:
            self._reactor.addWriter(sok, this.__next__)
            yield
            self._reactor.removeWriter(sok)
            sok.sendall(response)
            self._reactor.addReader(sok, this.__next__)
            yield
            self._reactor.removeReader(sok)
            command = sok.recv(1024).strip()
            if not command:
                sok.close()
                yield
            buff = StringIO()
            try:
                stdout_prev = sys.stdout
                stderr_prev = sys.stderr
                sys.stdout = buff
                sys.stderr = buff
                exec(command, self._globals)
            except:
                print_exc(limit=0)
            finally:
                sys.stdout = stdout_prev
                sys.stderr = stderr_prev
            response = buff.getvalue().encode() + PROMPT
