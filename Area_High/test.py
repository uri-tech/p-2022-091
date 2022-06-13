import socket

from HOST_PORT import HOSTPORT
from time import sleep


HOST, PORT = "localhost", 9999
data = "pleg is in the library"*1

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.bind((HOST,HOSTPORT['Satellite']))
    sock.connect((HOST, PORT))
    sleep(5)

    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

    sleep(5)

    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print(f"Sent:     {data}")
print(f"Received from the server:  {received}")