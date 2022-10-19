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
        self.assertAlmostEqual(max_integer([1, 2, 3, 4.89]), 4.89)

    def test_max_at_the_beginning(self):
        self.assertAlmostEqual(max_integer([100, 1, 3, 4.89]), 100)

    def one_negative_number(self):
        self.assertAlmostEqual(max_integer([100, -1, 3, 4.89]), 100)

    def only_negative_number(self):
        self.assertAlmostEqual(max_integer([-100, -1, -3, -4.89]), -1)

    def list_of_one_element(self):
        self.assertAlmostEqual(max_integer([-100]), -100)

    def list_is_empty(self):
        self.assertAlmostEqual(max_integer([]), 1)
