
try:
    from os import getenv
    # Low area
    HOST_LOW_AREA = getenv('HOST_LOW_AREA')
    if HOST_LOW_AREA is None:
        HOST_LOW_AREA = "localhost"
    PORT_LOW_AREA = getenv('PORT_LOW_AREA')
    if PORT_LOW_AREA is None:
        PORT_LOW_AREA = 8012
    # High area
    HOST_HIGH_AREA = getenv('HOST_HIGH_AREA')
    if HOST_HIGH_AREA is None:
        HOST_HIGH_AREA = "localhost"
    PORT_HIGH_AREA = getenv('PORT_HIGH_AREA')
    if PORT_HIGH_AREA is None:
        PORT_HIGH_AREA = 8022
    # Attacker
    HOST_ATTACKER = getenv('HOST_ATTACKER')
    if HOST_ATTACKER is None:
        HOST_ATTACKER = "localhost"
    PORT_ATTACKER = getenv('PORT_ATTACKER')
    if PORT_ATTACKER is None:
        PORT_ATTACKER = 8014
    # Server
    HOST_SERVER = getenv('HOST_SERVER')
    if HOST_SERVER is None:
        HOST_SERVER = "localhost"
    PORT_SERVER = getenv('PORT_SERVER')
    if PORT_SERVER is None:
        PORT_SERVER = 8030
except Exception as ex:
    raise Exception(f"Satellite-ERROR:\n{ex}")
