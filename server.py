from socket import socket, AF_INET, SOCK_STREAM
import json
import time


with open('common/conf.json') as conf_file:
    content = conf_file.read()
    conf_set = json.loads(content)
    port = conf_set['port']

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
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
