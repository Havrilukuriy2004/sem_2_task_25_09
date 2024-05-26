import socket

def client2_program():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            numbers = list(map(int, message.split()))
            min_num = min(numbers)
            max_num = max(numbers)
            response = f"Min: {min_num}, Max: {max_num}"
            client_socket.send(response.encode('utf-8'))
    except:
        client_socket.close()

if __name__ == '__main__':
    client2_program()
