## begin license ##
#
# All rights reserved.
#
# Copyright (C) 2011-2014 Seecr (Seek You Too B.V.) http://seecr.nl
#
## end license ##

import sys
from functools import partial
from traceback import print_exc

from weightless.http import Acceptor as TcpAcceptor
from weightless.udp import Acceptor as UdpAcceptor
from meresco.core import Observable


class _PacketListener(Observable):
    def __init__(self, reactor, port, acceptorClass):
        Observable.__init__(self)
        self._reactor = reactor
        self._port = port
        self._acceptorClass = acceptorClass

    def observer_init(self):
        def sinkFactory(sok):
            return lambda: self._handlePacket(sok)
        self._acceptorClass(
            reactor=self._reactor,
            port=self._port,
            sinkFactory=sinkFactory)

    def _handlePacket(self, sok):
        packet, remote = sok.recvfrom(2048)
        if type(self) is TcpPacketListener:
            while True:
                data = sok.recv(2048)
                if data == '':
                    break
                packet += data
        if remote is None:
            remote = sok.getpeername()
        try:
            self.do.handlePacket(data=packet, remote=remote)
        except Exception:
            print >> sys.stderr, "Exception in _handlePacket for data=%s from %s" % (repr(packet), remote)
            print_exc()
            sys.stderr.flush()
        finally:
            self.transmissionDone(sok)

    def transmissionDone(self, sok):
        pass


UdpPacketListener = partial(_PacketListener, acceptorClass=UdpAcceptor)


class TcpPacketListener(_PacketListener):
    def __init__(self, reactor, port):
        _PacketListener.__init__(self, reactor, port, acceptorClass=TcpAcceptor)

    def transmissionDone(self, sok):
        self._reactor.removeReader(sok)
        sok.close()
