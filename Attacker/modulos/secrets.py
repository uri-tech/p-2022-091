from HOST_PORT import HOSTPORT

try:
    HOST, PORT = "localhost", HOSTPORT['Attacker']
except Exception as ex:
    raise Exception(f"ERROR:\n{ex}")
