import socket
from time import sleep
from threading import Event


HOST, PORT = "localhost", 9999
data = "pleg is in the library"*1
# MAX_CONNECTION_TIME: tuple = tuple((114, 124))


received = "iiii"
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # sock.sendall(bytes(data + "\n", "utf-8"))
    sock.sendall(bytes([0x01])+bytes(data + "\n", "utf-8"))
    # Event().wait(8)
    sleep(1)
    # sock.sendall(bytes([0x01])+bytes(data + "\n", "utf-8"))
    # sock.sendall(bytes([0x01])+bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    # sock.sendall(bytes([0x01])+bytes(data + "\n", "utf-8"))
    # sock.send(bytes(0x01)+bytes(data + "\n", "utf-8"))  # (bytes([0x01])+bytes(data + "\n", "utf-8"))
    sleep(1)
    sock.sendall(bytes([0x01])+bytes(data + "\n", "utf-8"))
    # received = str(sock.recv(1024), "utf-8")
    # Event().wait(1)

    # while(True):
    #     pass
    # sleep(0.0001)
    # sock.sendall(bytes(data + "\n", "utf-8"))
    # # sleep(1)
    # sock.sendall(bytes(data + "\n", "utf-8"))
    # # sleep(1)
    # sock.sendall(bytes(data + "\n", "utf-8"))
    # sleep(1)

    # Receive data from the server and shut down
    # received = str(sock.recv(1024), "utf-8")

print(f"Sent:     {data}")
print(f"Received from the server: {received}")