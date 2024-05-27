from client_base import BaseClient
from protocol import CLIENT, BEGIN, QUESTION, ANSWER, END

class Client1(BaseClient):
    def run(self):
        self.send(CLIENT, "1")
        responses_received = 0
        while True:
            cmd, param = self.receive()
            if cmd == BEGIN:
                self.send_numbers()
            elif cmd == ANSWER:
                print(f"Received answer: {param}")
                responses_received += 1
                if responses_received == 2:
                    self.send(END)
                    break

    def send_numbers(self):
        print("Enter sequences of numbers separated by spaces (one per line). Enter an empty line to finish.")
        for _ in range(2):  # Expecting two lines of numbers
            line = input("Enter a sequence: ")
            self.send(QUESTION, line)

if __name__ == "__main__":
    Client1("localhost", 12346)
