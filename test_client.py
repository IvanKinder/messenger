import unittest
import client


class ServerTestCase(unittest.TestCase):

    def test_main(self):
        self.assertEqual(str(type(client.main())), "<class 'dict'>")


if __name__ == '__main__':
    unittest.main()
