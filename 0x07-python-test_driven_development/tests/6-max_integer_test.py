#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests the max value outputs are really correct or not """
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([-321, 2742, 3787, 14]), 3787)
        self.assertAlmostEqual(max_integer([-321, 1000002742, 7141143787,
                                            14]), 7141143787)
        self.assertAlmostEqual(max_integer([1000, 1000, 1000, 1000]), 1000)
        self.assertAlmostEqual(max_integer([452, 522, 654, 785, 654,
                                            231, 456, 201, 654, 352,
                                            635, 451, 6321, 231, 154,
                                            251, 632, 152, 654, 451,
                                            7141143787]), 7141143787)

    def test_float(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4.89]), 4)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_raise(self):
        self.assertRaises(TypeError, max_integer, max_integer([1, 2, 3, "4"]))
        self.assertRaises(KeyError, max_integer, max_integer({'a': 1, 'b': 2}))
