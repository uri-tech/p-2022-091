# pip install import_from_github_com
try:
    import logging
    import socketserver
    from modulos.network import CustomTCPHandler
    from modulos.secrets import HOST, PORT
    # from github_com.kennethreitz import requests
    # assert requests.get('https://github.com/p-2022-091/modulos/network.py').status_code == 200

    # formating the log
    FORMAT = '%(asctime)-15s %(nodeip)s %(type)-8s, message: %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'nodeip': 'ip', 'type': 'Satellite-Container'}
    logger = logging.getLogger('tcpserver')
    logger.setLevel(1)
except Exception as ex:
    raise Exception(f"Server-ERROR:\n{ex}")


if __name__ == '__main__':
    try:
        # Create the server, binding to ip HOST on PORT 
        with socketserver.ThreadingTCPServer((HOST, PORT), CustomTCPHandler) as server:
            logger.warning(f"Listening on {HOST} in port {PORT}", extra=d)
            # Activate the server; this will keep running until  interrupt the program with Ctrl-C
            server.serve_forever()

    except Exception as ex:
        raise Exception(f"Server-main: {ex}")
