from socket import socket, AF_INET, SOCK_STREAM
import select


def read_requests(r_list, clients):
    responses = {}
    for sock in r_list:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            clients.remove(sock)

    return responses


def write_responses(requests, w_list, clients):
    for sock in w_list:
        for _, request in requests.items():
            try:
                resp = request.encode('utf-8')
                sock.send(resp)
            except:
                sock.close()
                try:
                    clients.remove(sock)
                except ValueError:
                    pass


def mainloop():
    address = ('', 8888)
    clients = []

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            clients.append(conn)
        finally:
            r_list = []
            w_list = []
            try:
                r_list, w_list, e_list = select.select(clients, clients, [], 10)
            except:
                pass
            requests = read_requests(r_list, clients)
            if requests:
                write_responses(requests, w_list, clients)


print('start server')
mainloop()
