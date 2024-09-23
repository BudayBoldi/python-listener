import socket, threading

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 3306

def handle_messages(connection):
    print("Working!")

try:
    socket_instance = socket.socket()
    socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
    threading.Thread(target=handle_messages, args=[socket_instance]).start()
    while True:
            command = input(">")
            socket_instance.send(command.encode())
            # usage example: cmd.exe /c "Start calc.exe" or bash -c "gnome-calculator &"

except Exception as e:
    print(e)
