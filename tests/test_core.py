# -*- coding: utf-8 -*-

from functions import core

import unittest

HALLO = 'Hallo'


class CoreTestSuite(unittest.TestCase):

    def test_strcodes(self):
        self.assertListEqual(list(map(ord, HALLO)), core.strcodes(HALLO))

    def test_strsum(self):
        self.assertEqual(496, core.strsum(HALLO))

    def test_print_dict(self):
        added = core.add_dict({1: 111, 2: 222}, {2: 999, 3: 333})
        core.print_dict(added)
        self.assertDictEqual({1: 111, 2: 222, 3: 333}, added)

    def test_union(self):
        self.assertListEqual([1, 2, 3, 4], core.union([1, 2, 3], [3, 4]))

    def test_diff(self):
        self.assertListEqual([1, 2], core.diff([1, 2, 3], [3, 4]))

    def test_flatten(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], core.flatten([[[1, 2], 3], [[4]], (5, 6), ([7])]))


if __name__ == '__main__':
    unittest.main()
