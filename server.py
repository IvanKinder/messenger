from socket import socket, AF_INET, SOCK_STREAM
import time
import sys

from common import utils

host = ''
port = 0
default_host = ''

if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-p':
            port = int(sys.argv[i + 1])
        if sys.argv[i] == '-a':
            host = sys.argv[i + 1]

s = socket(AF_INET, SOCK_STREAM)

if port or host:
    s.bind((host, port))
    s.listen(5)
else:
    s.bind((default_host, utils.get_settings()['port']))
    s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(4096)
    print(utils.get_data_from_message(data))
    msg_json = {
        "action": "probe",
        "time": time.ctime(),
    }
    msg = utils.send_message(msg_json)
    client.send(msg.encode('utf-8'))
    client.close()
