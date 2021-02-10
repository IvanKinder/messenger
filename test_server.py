import unittest
from socket import socket, AF_INET, SOCK_STREAM

import server
from common.utils import get_data_from_message


class ServerTestCase(unittest.TestCase):

    def test_main(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('127.0.0.1', 7777))
        s.send(b'{"test": "test"}')
        self.assertEqual(get_data_from_message(s.recv(4096))['status'], 200)


if __name__ == '__main__':
    unittest.main()

