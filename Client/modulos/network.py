
try:
    # import logging
    import socket
    import threading
    import socketserver
    # import sys
except Exception as ex:
    raise Exception(f"ERROR:\n{ex}")


class CustomTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        try:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
        except Exception as ex:
            print(f"ERROR:\n{ex}")


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            data = str(self.request.recv(1024), 'ascii')
            cur_thread = threading.current_thread()
            response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
            self.request.sendall(response)
        except Exception as ex:
            print(f"ERROR:\n{ex}")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def client(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Received: {}".format(response))
        except Exception as ex:
            print(f"ERROR:\n{ex}")



class MyTcpHandler(socketserver.BaseRequestHandler):
    # BaseRequestHandler is specifically used to process communication-related information
    def handle(self):
        try:
            # Here must define a handle method, and the method name must be handle, sockerserver will automatically call the handle method
            print(self.request)  # The self.request here is equivalent to the conn object we saw before (conn,client_addr=server.accept())
            while True:
                try:
                    recv_cliend_cmd = self.request.recv(1024) # Receive instructions from the client
                    if not recv_cliend_cmd:
                        break
                        # Next, we will process the instructions sent by the client
                    obj = subprocess.Popen(recv_cliend_cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout = obj.stdout.read()
                    stderr = obj.stderr.read()
                    # Let's create the header (write it at will), here we really use the total_size in the dictionary
                    # header_dic={
                    #         'total_size':len(stdout)+len(stderr),
                    #         'filename':'xxx.mp4',
                    #         'md5sum':'8f6fbf8347faa4924a76856701edb0f3'
                    # }
                    # header_json = json.dumps(header_dic)
                    print(stderr)
                    # header_bytes = header_json.encode('utf-8')
                    # self.request.send(struct.pack('i', len(header_bytes)))  # This sent a fixed number of bytes in the past 4, so the client can receive four bytes for the first time
                    # self.request.send(header_bytes)
                    # self.request.send(stdout)
                    # self.request.send(stderr)
                    self.request.sendall(self.data.upper())

                except ConnectionResetError:
                    break
            self.request.close()
        except Exception as ex:
            print(f"ERROR:\n{ex}")


class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        try:
            # self.rfile is a file-like object created by the handler;
            # we can now use e.g. readline() instead of raw recv() calls
            self.data = self.rfile.readline().strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
            self.wfile.write(self.data.upper())
        except Exception as ex:
            print(f"ERROR:\n{ex}")