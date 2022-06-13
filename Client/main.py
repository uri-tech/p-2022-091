# # pip install import_from_github_com
# try:
#     import logging
#     import socketserver
#     from modulos.network import CustomTCPHandler
#     from modulos.secrets import HOST, PORT
#     # from github_com.kennethreitz import requests
#     # assert requests.get('https://github.com/p-2022-091/modulos/network.py').status_code == 200

#     # formating the log
#     FORMAT = '%(asctime)-15s %(nodeip)s %(type)-8s, message: %(message)s'
#     logging.basicConfig(format=FORMAT)
#     d = {'nodeip': 'ip', 'type': 'Satellite-Container'}
#     logger = logging.getLogger('tcpserver')
#     logger.setLevel(1)
# except Exception as ex:
#     raise Exception(f"ERROR:\n{ex}")


# if __name__ == '__main__':
#     try:
#         # Create the server, binding to ip HOST on PORT 
#         with socketserver.ThreadingTCPServer((HOST, PORT), CustomTCPHandler) as server:
#             # server.timeout = 5
#             # server.handle_timeout()
#             logger.warning(f"Listening on {HOST} in port {PORT}", extra=d)
#             # Activate the server; this will keep running until  interrupt the program with Ctrl-C
#             server.serve_forever()
#             # while True:
#             #     server.handle_request()
#     except Exception as ex:
#         raise Exception(f"main: {ex}")

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
