from client_base import BaseClient
from protocol import CLIENT, QUESTION, ANSWER, END

class Client2(BaseClient):
    def run(self):
        self.send(CLIENT, "2")
        while True:
            cmd, param = self.receive()
            if cmd == QUESTION:
                min_max = self.process_numbers(param)
                self.send(ANSWER, min_max)
            elif cmd == END:
                break

    def process_numbers(self, numbers):
        nums = list(map(int, numbers.split()))
        return f"{min(nums)} {max(nums)}"

if __name__ == "__main__":
    Client2("localhost", 12346)
