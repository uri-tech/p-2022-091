import socket

from HOST_PORT import HOSTPORT
from time import sleep


HOST, PORT_dst = "localhost", HOSTPORT['Area_High']
data = "pleg is in the library"*1

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.bind((HOST,HOSTPORT['Satellite']))
    sock.connect((HOST, PORT_dst))

    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

    

print(f"Sent:     {data}")
print(f"Received from the server:  {received}")