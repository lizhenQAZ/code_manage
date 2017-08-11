from twisted.internet import protocol, reactor
from time import ctime

port = 10001


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connect from:', clnt)

    def dataReceived(self, data):
        msg = '[%s] %s' % (ctime(), data.decode('utf-8'))
        self.transport.write(msg.encode('utf-8'))


def server_main():
    factory = protocol.Factory()
    factory.protocol = TSServProtocol
    reactor.listenTCP(port, factory)
    reactor.run()


if __name__ == '__main__':
    server_main()