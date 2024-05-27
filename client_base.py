import socket
from abc import ABCMeta, abstractmethod
from protocol import BaseDataExchangeProtocol

class BaseClient(BaseDataExchangeProtocol, metaclass=ABCMeta):
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))

        self.rfile = self.socket.makefile("rb", 0)
        self.wfile = self.socket.makefile("wb", 0)

        print(f"Connected to server {host}:{port}")
        self.run()
        self.finish()

    @abstractmethod
    def run(self):
        pass

    def finish(self):
        print("Connection to server closed")
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
