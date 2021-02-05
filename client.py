from socket import socket, AF_INET, SOCK_STREAM
import json
import time

with open('common/conf.json') as conf_file:
    content = conf_file.read()
    conf_set = json.loads(content)
    host = conf_set['host']
    port = conf_set['port']

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

msg_json = {
        "action": "presence",
        "time": time.ctime(),
        "type": "status",
        "user": {
                "account_name":  "C0deMaver1ck",
                "status":      "Yep, I am here!"
        }
}

msg = json.dumps(msg_json)
s.send(msg.encode('utf-8'))

data = s.recv(4096)
data_parse = json.loads(data)
print(f'action: {data_parse["action"]}\ntime: {data_parse["time"]}')

s.close()

