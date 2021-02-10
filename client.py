from socket import socket, AF_INET, SOCK_STREAM
import time
import sys

from common import utils


def main():
    host = ''
    port = 0
    if len(sys.argv) > 1:
        input_args = sys.argv[1].split(':')
        try:
            host = input_args[0]
            port = int(input_args[1])
        except IndexError:
            port = utils.get_settings()['port']

    s = socket(AF_INET, SOCK_STREAM)

    if port and host:
        s.connect((host, port))
    else:
        s.connect((utils.get_settings()['host'], utils.get_settings()['port']))

    msg_json = {
        "action": "presence",
        "time": time.ctime(),
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
        }
    }

    msg = utils.send_message(msg_json)
    s.send(msg.encode('utf-8'))

    data = s.recv(4096)
    data_parse = utils.get_data_from_message(data)
    print(data_parse)

    s.close()
    return data_parse


if __name__ == '__main__':
    main()
