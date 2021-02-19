from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)


def out_red(text):
    return "\033[31m{}" .format(text)


def out_white(text):
    return "\033[37m{}" .format(text)


def client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        my_choise = input('Если вы хотите принимать сообщения введите - 1;\nесли вводить сообщения - 2: ')
        while True:
            if my_choise == 'exit':
                break
            if my_choise == '2':
                print(out_white('Для закрытия соединения введите exit'))
                msg = input('Введите сообщение: ')
                if msg == 'exit':
                    my_choise = msg
                sock.send(msg.encode('utf-8'))
                data = sock.recv(1024).decode('utf-8')
                print(out_white(f'Информация с сервера: {out_red(data)}\n'))
            if my_choise == '1':
                data = sock.recv(1024).decode('utf-8')
                print(out_white(f'Информация с сервера: {out_red(data)}\n'))


if __name__ == '__main__':
    client()
