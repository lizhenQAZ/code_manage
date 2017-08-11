from twisted.internet import protocol, reactor


host = 'localhost'
port = 10001


# 1.创建协议类
class TSClntProtocol(protocol.Protocol):
    def senddata(self):
        data = input('>   ')
        if data:
            print(data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.senddata()

    def dataReceived(self, data):
        print(data)
        self.senddata()


# 2.创建工厂类
class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


def main():
    # 3.建立与TCP服务器的连接
    reactor.connectTCP(host, port, TSClntFactory())
    # 4.连接启动
    reactor.run()

if __name__ == '__main__':
    main()