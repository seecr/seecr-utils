## begin license ##
#
# All rights reserved.
#
# Copyright (C) 2012-2014 Seecr (Seek You Too B.V.) http://seecr.nl
#
## end license ##

from unittest import TestCase
import sys
from socket import socket, AF_INET, SOCK_DGRAM
from io import StringIO

from seecr.test import CallTrace
from weightless.core import compose, be
from meresco.core import Observable

from seecr.utils.packetlistener import UdpPacketListener, TcpPacketListener


class PacketListenerTest(TestCase):
    def testUdpPacketListener(self):
        reactor = CallTrace('reactor')
        observer = CallTrace('observer')
        udpPacketListener = UdpPacketListener(reactor, port=1234)
        server = be((Observable(),
            (udpPacketListener,
                (observer,)
            )
        ))
        list(compose(server.once.observer_init()))

        self.assertEqual('addReader', reactor.calledMethods[0].name)
        handleCallback = reactor.calledMethods[0].args[1]
        with socket(AF_INET, SOCK_DGRAM) as sok:
            sok.sendto(b"TEST", ('localhost', 1234))
        handleCallback()
        self.assertEqual(['observer_init', 'handlePacket'], observer.calledMethodNames())
        self.assertEqual(b"TEST", observer.calledMethods[1].kwargs['data'])

    def testTcpPacketListener(self):
        reactor = CallTrace('reactor')
        observer = CallTrace('observer')
        tcpPacketListener = TcpPacketListener(reactor, port=1234)
        server = be((Observable(),
            (tcpPacketListener,
                (observer,)
            )
        ))
        list(compose(server.once.observer_init()))

        self.assertEqual('addReader', reactor.calledMethods[0].name)
        acceptCallback = reactor.calledMethods[0].args[1]

        data = b"TEST" * 1024
        with socket() as sok:
            sok.connect(('localhost', 1234))
            bytesSent = sok.send(data)
            self.assertEqual(len(data), bytesSent)

        acceptCallback()
        self.assertEqual('addReader', reactor.calledMethods[1].name)
        handleCallback = reactor.calledMethods[1].args[1]
        handleCallback()

        self.assertEqual(['observer_init', 'handlePacket'], observer.calledMethodNames())
        self.assertEqual(data, observer.calledMethods[1].kwargs['data'])
        self.assertEqual('removeReader', reactor.calledMethods[2].name)

    def testExceptionInDownstreamHandlePacket(self):
        server = UdpPacketListener(reactor=None, port=1234)
        sok = CallTrace(returnValues={'recvfrom': (b'data', ('127.0.0.1', 1234))})
        observer = CallTrace()
        observer.exceptions['handlePacket'] = Exception("This should be happening")
        server.addObserver(observer)

        mockStderr = StringIO()
        sys.stderr = mockStderr
        try:
            server._handlePacket(sok)
        finally:
            sys.stderr = sys.__stderr__
        lines = mockStderr.getvalue().split('\n')
        self.assertEqual("Exception in _handlePacket for data=b'data' from ('127.0.0.1', 1234)", lines[0])
        self.assertEqual('Traceback (most recent call last):', lines[1])
        self.assertEqual('Exception: This should be happening', lines[-2])
