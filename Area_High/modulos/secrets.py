
from HOST_PORT import HOSTPORT

try:
    HOST, PORT = "localhost", HOSTPORT['Area_High']
except Exception as ex:
    raise Exception(f"ERROR:\n{ex}")
