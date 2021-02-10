import unittest

from common.utils import get_data_from_message, send_message, get_settings


class ServerTestCase(unittest.TestCase):

    def test_get_data_from_message(self):
        result = get_data_from_message(b'{"test": "test"}')
        self.assertEqual(result, {'test': 'test'})

    def test_send_message(self):
        result = send_message({'test': 'test'})
        self.assertEqual(result, '{"test": "test"}')

    def test_get_settings(self):
        result = get_settings()
        self.assertEqual(result, {
            "host": "127.0.0.1",
            "port": 7777
        })


if __name__ == '__main__':
    unittest.main()
