import socket
import threading

def handle_client(client_socket, client_id, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if client_id == 1:
                clients[2].send(message.encode('utf-8'))
            elif client_id == 2:
                clients[1].send(message.encode('utf-8'))
        except:
            client_socket.close()
            break

def server_program():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    clients = {}

    print("Server is listening...")

    for i in range(1, 3):
        client_socket, addr = server_socket.accept()
        print(f"Connection from Client {i}: {addr}")
        clients[i] = client_socket
        threading.Thread(target=handle_client, args=(client_socket, i, clients)).start()

if __name__ == '__main__':
    server_program()
