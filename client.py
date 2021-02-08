from socket import socket, AF_INET, SOCK_STREAM
import json
import time
import sys

with open('common/conf.json') as conf_file:
    content = conf_file.read()
    conf_set = json.loads(content)
    default_host = conf_set['host']
    default_port = conf_set['port']

host = ''
port = 0

if len(sys.argv) > 1:
    input_args = sys.argv[1].split(':')


s = socket(AF_INET, SOCK_STREAM)
if port and host:
    s.connect((host, port))
else:
    s.connect((default_host, default_port))

msg_json = {
    "action": "presence",
    "time": time.ctime(),
    "type": "status",
    "user": {
        "account_name": "C0deMaver1ck",
        "status": "Yep, I am here!"
    }
}

msg = json.dumps(msg_json)
s.send(msg.encode('utf-8'))

data = s.recv(4096)
data_parse = json.loads(data)
print(f'action: {data_parse["action"]}\ntime: {data_parse["time"]}')

s.close()
