import unittest
from socket import socket, AF_INET, SOCK_STREAM
import time
import sys

from common import utils
from common.utils import get_data_from_message


def main():
    host = ''
    port = 0
    default_host = ''
    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-p':
                if 1024 <= int(sys.argv[i + 1]) <= 65535:
                    port = int(sys.argv[i + 1])
                else:
                    print(f'use default port: {utils.get_settings()["port"]}')
                    port = utils.get_settings()['port']
            elif '-p' not in sys.argv:
                print(f'use default port: {utils.get_settings()["port"]}')
                port = utils.get_settings()['port']
            if sys.argv[i] == '-a':
                host = sys.argv[i + 1]
            elif '-a' not in sys.argv:
                print(f'use default host: {utils.get_settings()["host"]}')
                host = utils.get_settings()['host']

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
            "status": 200
        }
        msg = utils.send_message(msg_json)
        client.send(msg.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()
