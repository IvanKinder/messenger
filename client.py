import logging
from socket import socket, AF_INET, SOCK_STREAM
import time
import sys
from log.client import client_log_config
from common import utils

logger = logging.getLogger('client_log_app')


def main():
    host = ''
    port = 0
    if len(sys.argv) > 1:
        input_args = sys.argv[1].split(':')
        try:
            host = input_args[0]
            port = int(input_args[1])
        except IndexError:
            logger.warning(f'incorrect port: {port}! Use default: {utils.get_settings()["port"]}')
            port = utils.get_settings()['port']
        except ValueError:
            logger.warning(f'incorrect port: {port}')

    s = socket(AF_INET, SOCK_STREAM)

    if port and host:
        try:
            s.connect((host, port))
        except:
            logger.critical(f'incorrect host: {host}')
    else:
        logger.info(f'use default host: {utils.get_settings()["host"]} and default port: {utils.get_settings()["port"]}')
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
    try:
        s.send(msg.encode('utf-8'))
    except BrokenPipeError:
        logger.critical(f'incorrect host: {host}')

    try:
        data = s.recv(4096)
        data_parse = utils.get_data_from_message(data)
        print(data_parse)
        s.close()
        return data_parse
    except OSError:
        logger.critical(f'incorrect host: {host}')


if __name__ == '__main__':
    main()
