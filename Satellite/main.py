
try:
    import socket
    from time import time
    from random import uniform, randint, shuffle
    from modulos.secrets import HOST_HIGH_AREA, PORT_HIGH_AREA
    # from github_com "" import requests
    # assert requests.get('https://github.com/p-2022-091/modulos/network.py').status_code == 200
    import signal

    # # formating the log
    # import logging
    # FORMAT = '%(asctime)-15s %(nodeip)s %(type)-8s, message: %(message)s'
    # logging.basicConfig(format=FORMAT)
    # d = {'nodeip': 'ip', 'type': 'Satellite-Container'}
    # logger = logging.getLogger('tcpserver')
    # logger.setLevel(1)
except Exception as ex:
    raise Exception(f"Satellite-ERROR:\n{ex}")


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")


if __name__ == '__main__':
    try:
        NUM_OF_SATELLITE: int = 1000
        SATELLITE_ID_LIST: list = list(
            range(2000000000, 2000000000 + NUM_OF_SATELLITE, 1)
        )
        shuffle(SATELLITE_ID_LIST)
        SATELLITE_START_dBm: str = "4444dBm"

        while True:
            SATELLITE_MIGRATION_TIME: float = uniform(100, 130)
            idxSatelliteId: int = randint(0, NUM_OF_SATELLITE)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.settimeout(SATELLITE_MIGRATION_TIME)
                sock.connect((HOST_HIGH_AREA, int(PORT_HIGH_AREA)))
                start_time = time()
                sock.sendall(
                    bytes(
                        SATELLITE_START_dBm
                        + str(SATELLITE_ID_LIST[idxSatelliteId])
                        + "1" * 100
                        + "\n",
                        "utf-8",
                    )
                )

                # Set the signal handler and a 5-second alarm
                # signal.setitimer(signal.SIGABRT, 5, interval=5.0)
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(5)

                # Receive data from the server and shut dow
                received = str(sock.recv(1024), "utf-8")
                print(f"received: {received}")

                # leave the connection open until the migration time pass
                while(sock.gettimeout() > time()-start_time):
                    pass
            # Handles in case we have gone through all the satellites already
            tempIdxSatelliteId: int = randint(0, NUM_OF_SATELLITE)
            while(tempIdxSatelliteId == idxSatelliteId):
                tempIdxSatelliteId: int = randint(0, NUM_OF_SATELLITE)
            idxSatelliteId = tempIdxSatelliteId
    except Exception as ex:
        print(f"Satellite-main: {ex}")
