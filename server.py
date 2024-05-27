import socketserver
from protocol import BaseDataExchangeProtocol, CLIENT, BEGIN, QUESTION, ANSWER, END, MESSAGE


class Server(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, handler_class):
        self.client = {1: None, 2: None}
        super().__init__(server_address, handler_class)


class RequestHandler(socketserver.StreamRequestHandler, BaseDataExchangeProtocol):
    def handle(self):
        self.no = None
        print(f"Connected: {self.client_address}")
        try:
            cmd, param = self.receive()
            client_id = int(param)
            if cmd == CLIENT and client_id in (1, 2) and self.server.client[client_id] is None:
                self.no = client_id
                self.server.client[client_id] = self
                self.send(MESSAGE, f"Connected as client {client_id}")
                if all(self.server.client.values()):
                    self.server.client[1].send(BEGIN)
            else:
                self.send(END, "Connection error")
                return

            while True:
                cmd, param = self.receive()
                if cmd == BEGIN:
                    self.server.client[2].send(BEGIN)
                elif cmd == QUESTION:
                    self.server.client[2].send(QUESTION, param)
                elif cmd == ANSWER:
                    self.server.client[1].send(ANSWER, param)
                elif cmd == END:
                    break
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.finish()

    def finish(self):
        if self.no:
            self.server.client[self.no] = None
            print(f"Disconnected: {self.client_address} as client {self.no}")
        self.request.shutdown(socket.SHUT_RDWR)
        self.request.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 12346
    with Server((HOST, PORT), RequestHandler) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
