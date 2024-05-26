import socket

def client1_program():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            data = input("Enter a sequence of integers (separated by spaces): ")
            client_socket.send(data.encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received from Client 2: {response}")
    except:
        client_socket.close()

if __name__ == '__main__':
    client1_program()
