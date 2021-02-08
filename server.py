from socket import socket, AF_INET, SOCK_STREAM
import json
import time
import sys


host = ''
port = 0
default_host = ''

with open('common/conf.json') as conf_file:
    content = conf_file.read()
    conf_set = json.loads(content)
    default_port = conf_set['port']

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
    s.bind((default_host, default_port))
    s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(4096)
    print(data.decode('utf-8'))
    msg_json = {
        "action": "probe",
        "time": time.ctime(),
    }
    msg = json.dumps(msg_json)
    client.send(msg.encode('utf-8'))
    client.close()
