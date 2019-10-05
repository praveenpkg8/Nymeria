import unittest

from twitter_bot import hello_world

class TestBot(unittest.TestCase):

    def test_hello_world(self):
        self.assertIsNotNone(hello_world())

if __name__ == '__main__':
    unittest.main()