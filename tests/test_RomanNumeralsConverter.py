#!python2
# coding: utf-8

"""
Tests for RomanNumeralsConverter.py
"""


import unittest
from RomanNumeralsConverter import is_possible_roman_numeral


class TestIsPossibleRomanNumeral(unittest.TestCase):
    """
    is_possible_roman_numeral(string)
    """
    def test_empty_string(self):
        self.assertFalse(is_possible_roman_numeral(""))

    def test_digits(self):
        self.assertFalse(is_possible_roman_numeral("0123456789"))

    def test_symbols(self):
        self.assertFalse(is_possible_roman_numeral("!#$%%&()=?/\\"))

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

    def test_new_line(self):
        self.assertFalse(is_possible_roman_numeral("M\nC"))


class TestIsNonZeroArabicNumeral(unittest.TestCase):  # TODO
    """
    is_non_zero_arabic_numeral(string)
    """
    pass
