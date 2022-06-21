# pip install import_from_github_com
try:
    import logging
    from datetime import datetime, timedelta
    import threading
    # from modulos.secrets import HOST, PORT
    import socket
    from time import time
    from random import uniform, randint, shuffle
    from modulos.secrets import HOST_LOW_AREA, PORT_LOW_AREA
    # from github_com.kennethreitz import requests
    # assert requests.get('https://github.com/p-2022-091/modulos/network.py').status_code == 200
    
    # formating the log
    FORMAT = '%(asctime)-15s %(nodeip)s %(type)-8s, message: %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'nodeip': 'ip', 'type': 'Client-Container'}
    logger = logging.getLogger('tcpserver')
    logger.setLevel(1)

except Exception as ex:
    raise Exception(f"ERROR:\n{ex}")


def ClientThread(client_id: str):
    try:
        CLIENT_START_dBm: str = "4444dBm"
        print(f"HOST_LOW_AREA: {'10.106.149.84'}, PORT_LOW_AREA:{PORT_LOW_AREA}")
        while(True):
            CLIENT_MIGRATION_TIME: float = uniform(100, 130)
            temp_time = int((datetime.now() + timedelta(seconds=CLIENT_MIGRATION_TIME)).strftime("%Y%m%d%H%M%S"))
            idxClientId: int = randint(0, NUM_OF_CLIENT)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.settimeout(CLIENT_MIGRATION_TIME)
                sock.connect(("10.106.149.84", int(PORT_LOW_AREA)))
                start_time = time()
                sock.sendall(bytes(str(CLIENT_START_dBm) + str(CLIENT_ID_LIST[idxClientId]) + str(temp_time) + "1"*100 + "\n", "utf-8"))
                # Receive data from the server and shut dow
                received = str(sock.recv(1024), "utf-8")
                print(f"received data: {received}")

                while(sock.gettimeout() > time()-start_time):
                    pass
            tempIdxClientId: int = randint(0, NUM_OF_CLIENT)
            while(tempIdxClientId == idxClientId):
                tempIdxClientId: int = randint(0, NUM_OF_CLIENT)
            idxClientId = tempIdxClientId
    except Exception as ex:
        print(f"Client-ClientThread: {ex}")


if __name__ == '__main__':
    try:
        NUM_OF_CLIENT: int = 1000
        CLIENT_ID_LIST: list = [i for i in range(1000000000, 1000000000+NUM_OF_CLIENT, 1)]
        shuffle(CLIENT_ID_LIST)
        idxClientId: int = 0
        while(True):
            if(idxClientId >= NUM_OF_CLIENT):
                idxClientId = 0
            while(threading.active_count() != NUM_OF_CLIENT):
                client_t = threading.Thread(target=ClientThread, args=(str(CLIENT_ID_LIST[idxClientId]),), daemon=True)
                client_t.start()
            idxClientId += 1
    except Exception as ex:
        print(f"Client-main: {ex}")
