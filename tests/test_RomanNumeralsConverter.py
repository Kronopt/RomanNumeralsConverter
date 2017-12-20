#!python2
# coding: utf-8

"""
Tests for RomanNumeralsConverter.py
"""


import unittest
from RomanNumeralsConverter import (is_possible_roman_numeral,
                                    is_non_zero_arabic_numeral)


class TestIsPossibleRomanNumeral(unittest.TestCase):
    """
    is_possible_roman_numeral(string)
    """
    def test_empty_string(self):
        self.assertFalse(is_possible_roman_numeral(""))

    def test_digits(self):
        self.assertFalse(is_possible_roman_numeral("0123456789"))

    def test_symbols(self):
        self.assertFalse(is_possible_roman_numeral("!#$%&()=?/\\"))

    def test_lower_case(self):
        self.assertTrue(is_possible_roman_numeral("IVXLCDM"))

    def test_upper_case(self):
        self.assertTrue(is_possible_roman_numeral("ivxlcdm"))

    def test_mixed_case(self):
        self.assertTrue(is_possible_roman_numeral("iIvVxXlLcCdDmM"))

    def test_wrong_char_at_start(self):
        self.assertFalse(is_possible_roman_numeral(" XXXI"))

    def test_wrong_char_at_end(self):
        self.assertFalse(is_possible_roman_numeral("XXXI "))

    def test_wrong_char_at_middle(self):
        self.assertFalse(is_possible_roman_numeral("XX XI"))

    def test_1_char(self):
        self.assertTrue(is_possible_roman_numeral("I"))

    def test_10_chars(self):
        self.assertTrue(is_possible_roman_numeral("IIIIIIIIII"))

    def test_15_chars(self):
        self.assertFalse(is_possible_roman_numeral("IIIIIIIIIIIIIII"))

    def test_new_line(self):
        self.assertFalse(is_possible_roman_numeral("M\nC"))


class TestIsNonZeroArabicNumeral(unittest.TestCase):
    """
    is_non_zero_arabic_numeral(string)
    """
    def test_empty_string(self):
        self.assertFalse(is_non_zero_arabic_numeral(""))

    def test_not_digit(self):
        self.assertFalse(is_non_zero_arabic_numeral("a#/."))

    def test_zero(self):
        self.assertFalse(is_non_zero_arabic_numeral("0"))

    def test_zeroes(self):
        self.assertFalse(is_non_zero_arabic_numeral("000000000000000"))

    def test_negative(self):
        self.assertFalse(is_non_zero_arabic_numeral("-1"))

    def test_positive(self):
        self.assertTrue(is_non_zero_arabic_numeral("1"))

    def test_over_max(self):
        self.assertFalse(is_non_zero_arabic_numeral("3900"))

    def test_middle(self):
        self.assertTrue(is_non_zero_arabic_numeral("2000"))


class TestAtMostOnceVLD(unittest.TestCase):  # TODO
    """
    at_most_once_vld(string)
    """


# TODO assertRaises for wrong type
