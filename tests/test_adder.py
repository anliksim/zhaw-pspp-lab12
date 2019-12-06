from functions import adder

import unittest


class AdderTestSuite(unittest.TestCase):

    def test_adder(self):
        self.assertEqual(3, adder.add(1, 2))


if __name__ == '__main__':
    unittest.main()
