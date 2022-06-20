

try:
    # import logging
    import socket
    import socketserver
    # import sys
except Exception as ex:
    raise Exception(f"ERROR:\n{ex}")

client_sid = 1000000000
client_max_device = 10000

satellite_sid = 2000000000
satellite_max_device = 10000


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
            
            print("{} wrote:".format(self.client_address[1]))
            print(self.data)
            low_db = 2
            data_byte = lower_snr(self.data, low_db)
            print(data_byte)
            # Send forward the same data, with lower snr
            # if(self.client_address[1] == HOSTPORT['Satellite']):
            #     print("Forward Lower")
            #     forward_socket(HOSTPORT['Area_High_OUT'],HOSTPORT['Area_Low'],data_byte)
            #     forward_socket(HOSTPORT['Area_High_OUT'],HOSTPORT['Attacker'],data_byte)
            # else:
            #     forward_socket(HOSTPORT['Area_High_OUT'],HOSTPORT['Satellite'],data_byte)

            if satellite_sid < satellite_sid < satellite_sid + satellite_max_device:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(("localhost", 8014))
                    sock.sendall(data_byte)

        except Exception as ex:
            print(f"ERROR:\n{ex}")


def lower_snr(data, lower_db, which_byte=0):
    # byte_data = bytes(data, 'utf-8')
    byte_data = list(data)
    byte_data[which_byte] = byte_data[which_byte] - lower_db
    return bytes(byte_data)


def forward_socket(src_port, dst_port, data):
    HOST = "localhost"
    # Create a socket (SOCK_STREAM means a TCP socket)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.bind((HOST, src_port))
        sock.connect((HOST, dst_port))
        sock.sendall(data)
        print(f"Sent FROM:  {src_port} ==> TO:  {dst_port}")
    except Exception as ex:
        print(f"ERROR:\n{ex}")