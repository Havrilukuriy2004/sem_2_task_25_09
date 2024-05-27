CLIENT = "CLIENT"
BEGIN = "BEGIN"
MESSAGE = "MESSAGE"
QUESTION = "QUESTION"
ANSWER = "ANSWER"
END = "END"

class BaseDataExchangeProtocol:
    def receive(self):
        data = self.rfile.readline().decode("utf-8").strip()
        parts = data.split(" ", 1)
        if len(parts) == 2:
            cmd, param = parts
        else:
            cmd, param = parts[0], ""
        return cmd, param

    def send(self, cmd, param=""):
        message = f"{cmd} {param}\n"
        self.wfile.write(message.encode("utf-8"))
