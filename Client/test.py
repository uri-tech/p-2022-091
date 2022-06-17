import socket
from time import time
from random import uniform


if __name__ == '__main__':
    try:
        HOST, PORT = "localhost", 9999
        # SATELLITE_MIGRATION_TIME: float = uniform(100, 130)
        data = bytes("dbm"+"7777777"+"1"*10, "utf-8")
        print(f"type: {type(data)}, __sizeof__: {(data.__sizeof__())}")

        # Create a socket (SOCK_STREAM means a TCP socket)
        # create_connection() -- connects to an address, with an optional timeout and
        # with socket.create_connection(socket.AF_INET, socket.SOCK_STREAM, timeout=10.0) as sock:

        while(True):
            SATELLITE_MIGRATION_TIME: float = uniform(100, 130)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.settimeout(SATELLITE_MIGRATION_TIME)
                # sock.setdefaulttimeout(3)
                sock.connect((HOST, PORT))
                start_time = time()
                sock.sendall(bytes(data + "\n", "utf-8"))

                # Receive data from the server and shut dow
                received = str(sock.recv(1024), "utf-8")
                sock.sendall(bytes(data + "\n", "utf-8"))
                print(f"sock.gettimeout(): {sock.gettimeout()}, time():{time()}, start_time: {start_time}, {time()-start_time}")
                while(sock.gettimeout() > time()-start_time):
                    pass

            print(f"Sent:     {data}")
            print(f"Received from the server:  {received}")
    except Exception as ex:
        raise Exception(f"main: {ex}")
