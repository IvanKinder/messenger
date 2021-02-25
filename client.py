from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import json

address = ('localhost', 8888)


def out_red(text):
    return "\033[31m{}" .format(text)


def out_white(text):
    return "\033[37m{}" .format(text)


def send_msg(sock):
    msg = {'msg': input(), 'sender': str(sock)}
    json_msg = json.dumps(msg)
    sock.send(json_msg.encode('utf-8'))
    print('отправлено...')


def recv_msg(sock):
    json_data = sock.recv(1024).decode('utf-8')
    data = json.loads(json_data)
    if data['sender'] != str(sock):
        print(out_white(f'\nИнформация с сервера: {out_red(data["msg"])}') + out_white(''))


class SendMsg(Thread):
    def __init__(self, sock):
        super().__init__()
        self.daemon = True
        self.sock = sock

    def run(self):
        while True:
            send_msg(self.sock)


class RecvMsg(Thread):
    def __init__(self, sock):
        super().__init__()
        self.daemon = True
        self.sock = sock

    def run(self):
        while True:
            recv_msg(self.sock)


def main():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        r = RecvMsg(sock)
        s = SendMsg(sock)
        print('Вводите сообщение когда захотите:')
        r.start()
        s.start()
        r.join()
        s.join()


if __name__ == '__main__':
    main()


# def client():
#     with socket(AF_INET, SOCK_STREAM) as sock:
#         sock.connect(address)
#         my_choise = input('Если вы хотите принимать сообщения введите - 1;\nесли вводить сообщения - 2: ')
#         while True:
#             if my_choise == 'exit':
#                 break
#             if my_choise == '2':
#                 print(out_white('Для закрытия соединения введите exit'))
#                 msg = input('Введите сообщение: ')
#                 if msg == 'exit':
#                     my_choise = msg
#                 sock.send(msg.encode('utf-8'))
#                 data = sock.recv(1024).decode('utf-8')
#                 print(out_white(f'Информация с сервера: {out_red(data)}\n'))
#             if my_choise == '1':
#                 data = sock.recv(1024).decode('utf-8')
#                 print(out_white(f'Информация с сервера: {out_red(data)}\n'))