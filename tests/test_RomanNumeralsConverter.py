#!python2
# coding: utf-8

"""
Tests for RomanNumeralsConverter.py
"""


import unittest
from RomanNumeralsConverter import (is_possible_roman_numeral,
                                    is_non_zero_arabic_numeral,
                                    at_most_once_vld,
                                    at_most_3_in_row_ixcm,
                                    find_subtractive_combinations,
                                    subtractive_combination_validity,
                                    roman_to_arabic,
                                    arabic_to_roman)


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


class TestAtMostOnceVLD(unittest.TestCase):
    """
    at_most_once_vld(string)
    """
    def test_v(self):
        self.assertTrue(at_most_once_vld("V"))

    def test_l(self):
        self.assertTrue(at_most_once_vld("L"))

    def test_d(self):
        self.assertTrue(at_most_once_vld("D"))

    def test_vv(self):
        self.assertFalse(at_most_once_vld("VV"))

    def test_ll(self):
        self.assertFalse(at_most_once_vld("LL"))

    def test_dd(self):
        self.assertFalse(at_most_once_vld("DD"))

    def test_vld(self):
        self.assertTrue(at_most_once_vld("VLD"))

    def test_v_other_chars(self):
        self.assertTrue(at_most_once_vld("XXXVIII"))

    def test_l_other_chars(self):
        self.assertTrue(at_most_once_vld("CLXXIII"))

    def test_d_other_chars(self):
        self.assertTrue(at_most_once_vld("MDCXXII"))


class TestAtMost3InRowIXCM(unittest.TestCase):
    """
    at_most_3_in_row_ixcm(string)
    """
    def test_i(self):
        self.assertTrue(at_most_3_in_row_ixcm("I"))

    def test_x(self):
        self.assertTrue(at_most_3_in_row_ixcm("X"))

    def test_c(self):
        self.assertTrue(at_most_3_in_row_ixcm("C"))

    def test_m(self):
        self.assertTrue(at_most_3_in_row_ixcm("M"))

    def test_iii(self):
        self.assertTrue(at_most_3_in_row_ixcm("III"))

    def test_xxx(self):
        self.assertTrue(at_most_3_in_row_ixcm("XXX"))

    def test_ccc(self):
        self.assertTrue(at_most_3_in_row_ixcm("CCC"))

    def test_mmm(self):
        self.assertTrue(at_most_3_in_row_ixcm("MMM"))

    def test_iiii(self):
        self.assertFalse(at_most_3_in_row_ixcm("IIII"))

    def test_xxxx(self):
        self.assertFalse(at_most_3_in_row_ixcm("XXXX"))

    def test_cccc(self):
        self.assertFalse(at_most_3_in_row_ixcm("CCCC"))

    def test_mmmm(self):
        self.assertFalse(at_most_3_in_row_ixcm("MMMM"))

    def test_i_pairs(self):
        self.assertTrue(at_most_3_in_row_ixcm("IIXIICII"))

    def test_x_pairs(self):
        self.assertTrue(at_most_3_in_row_ixcm("XXDXXLXX"))

    def test_c_pairs(self):
        self.assertTrue(at_most_3_in_row_ixcm("CCMCCLCC"))

    def test_m_pairs(self):
        self.assertTrue(at_most_3_in_row_ixcm("MMCMMDMM"))

    def test_IIII_at_end(self):
        self.assertFalse(at_most_3_in_row_ixcm("CCMMIILLXXIICCLLIIII"))

    def test_XXXX_at_end(self):
        self.assertFalse(at_most_3_in_row_ixcm("CCMMIILLXXIICCLLXXXX"))

    def test_CCCC_at_end(self):
        self.assertFalse(at_most_3_in_row_ixcm("CCMMIILLXXIICCLLCCCC"))

    def test_MMMM_at_end(self):
        self.assertFalse(at_most_3_in_row_ixcm("CCMMIILLXXIICCLLMMMM"))


class TestFindSubtractiveCombinations(unittest.TestCase):
    """
    find_subtractive_combinations
    """
    def test_iv(self):
        self.assertEquals(find_subtractive_combinations("IV"), (("IV", 0), ))

    def test_ix(self):
        self.assertEquals(find_subtractive_combinations("IX"), (("IX", 0), ))

    def test_xl(self):
        self.assertEquals(find_subtractive_combinations("XL"), (("XL", 0), ))

    def test_xc(self):
        self.assertEquals(find_subtractive_combinations("XC"), (("XC", 0), ))

    def test_cd(self):
        self.assertEquals(find_subtractive_combinations("CD"), (("CD", 0), ))

    def test_cm(self):
        self.assertEquals(find_subtractive_combinations("CM"), (("CM", 0), ))

    def test_xiv(self):
        self.assertEquals(find_subtractive_combinations("XIV"), (("IV", 1), ))

    def test_xix(self):
        self.assertEquals(find_subtractive_combinations("XIX"), (("IX", 1), ))

    def test_cxl(self):
        self.assertEquals(find_subtractive_combinations("CXL"), (("XL", 1), ))

    def test_cxc(self):
        self.assertEquals(find_subtractive_combinations("CXC"), (("XC", 1), ))

    def test_mcd(self):
        self.assertEquals(find_subtractive_combinations("MCD"), (("CD", 1), ))

    def test_mcm(self):
        self.assertEquals(find_subtractive_combinations("MCM"), (("CM", 1), ))

    def test_ccxciv(self):
        self.assertEquals(find_subtractive_combinations("CCXCIV"), (("XC", 2), ("IV", 4), ))

    def test_xliv(self):
        self.assertEquals(find_subtractive_combinations("XLIV"), (("XL", 0), ("IV", 2), ))

    def test_cmxliv(self):
        self.assertEquals(find_subtractive_combinations("CMXLIV"), (("CM", 0), ("XL", 2), ("IV", 4), ))

    def test_i(self):
        self.assertEquals(find_subtractive_combinations("I"), ())

    def test_xxx(self):
        self.assertEquals(find_subtractive_combinations("XXX"), ())

    def test_mmmcccxxxviii(self):
        self.assertEquals(find_subtractive_combinations("MMMCCCXXXVIII"), ())


class TestSubtractiveCombinationValidity(unittest.TestCase):
    """
    subtractive_combination_validity
    """
    def test_iv(self):
        self.assertTrue(subtractive_combination_validity((("IV", 0), )))

    def test_ix(self):
        self.assertTrue(subtractive_combination_validity((("IX", 0), )))

    def test_xl(self):
        self.assertTrue(subtractive_combination_validity((("XL", 0), )))

    def test_xc(self):
        self.assertTrue(subtractive_combination_validity((("XC", 0), )))

    def test_cd(self):
        self.assertTrue(subtractive_combination_validity((("CD", 0), )))

    def test_cm(self):
        self.assertTrue(subtractive_combination_validity((("CM", 0), )))

    def test_il(self):
        self.assertFalse(subtractive_combination_validity((("IL", 0), )))

    def test_ic(self):
        self.assertFalse(subtractive_combination_validity((("IC", 0), )))

    def test_id(self):
        self.assertFalse(subtractive_combination_validity((("ID", 0), )))

    def test_im(self):
        self.assertFalse(subtractive_combination_validity((("IM", 0), )))

    def test_xd(self):
        self.assertFalse(subtractive_combination_validity((("XD", 0), )))

    def test_xm(self):
        self.assertFalse(subtractive_combination_validity((("XM", 0), )))


class TestRomanToArabic(unittest.TestCase):
    """
    roman_to_arabic(roman_numeral)
    """
    def test_not_string(self):
        self.assertRaises(TypeError, roman_to_arabic, 1)

    def test_lower_case(self):
        self.assertEquals(roman_to_arabic("i"), 1)

    def test_lower_case_2(self):
        self.assertEquals(roman_to_arabic("xxiv"), 24)

    def test_mixed_case(self):
        self.assertEquals(roman_to_arabic("mMmccCXXXviii"), 3338)

    def test_i(self):
        self.assertEquals(roman_to_arabic("I"), 1)

    def test_v(self):
        self.assertEquals(roman_to_arabic("V"), 5)

    def test_x(self):
        self.assertEquals(roman_to_arabic("X"), 10)

    def test_l(self):
        self.assertEquals(roman_to_arabic("L"), 50)

    def test_c(self):
        self.assertEquals(roman_to_arabic("C"), 100)

    def test_d(self):
        self.assertEquals(roman_to_arabic("D"), 500)

    def test_m(self):
        self.assertEquals(roman_to_arabic("M"), 1000)

    def test_iv(self):
        self.assertEquals(roman_to_arabic("IV"), 4)

    def test_ix(self):
        self.assertEquals(roman_to_arabic("IX"), 9)

    def test_xl(self):
        self.assertEquals(roman_to_arabic("XL"), 40)

    def test_xc(self):
        self.assertEquals(roman_to_arabic("XC"), 90)

    def test_cd(self):
        self.assertEquals(roman_to_arabic("CD"), 400)

    def test_cm(self):
        self.assertEquals(roman_to_arabic("CM"), 900)

    def test_max_roman_numeral(self):
        self.assertEquals(roman_to_arabic("MMMDCCCXCIX"), 3899)

    def test_longest_roman_numeral(self):
        self.assertEquals(roman_to_arabic("MMDCCCLXXXVIII"), 2888)

    def test_wrong_numeral_clxvc(self):
        self.assertEquals(roman_to_arabic("CLXVC"), -1)

    def test_wrong_numeral_ixx(self):
        self.assertEquals(roman_to_arabic("IXX"), -1)

    def test_wrong_numeral_civm(self):
        self.assertEquals(roman_to_arabic("CIVM"), -1)

    def test_wrong_numeral_mmmcdm(self):
        self.assertEquals(roman_to_arabic("MMMCDM"), -1)

    # TODO correct the following cases

    # def test_wrong_numeral_ivi(self):
    #     self.assertEquals(roman_to_arabic("IVI"), -1)
    #
    # def test_wrong_numeral_xcx(self):
    #     self.assertEquals(roman_to_arabic("XCX"), -1)

    # TODO more wrong cases


# class TestArabicToRoman(unittest.TestCase):
#     """
#     arabic_to_roman(arabic_numeral)
#     """
#     def test_not_integer(self):
#         self.assertRaises(TypeError, arabic_to_roman, "1")
#
#     def test_1(self):
#         self.assertEquals(arabic_to_roman(1), "I")
#
#     def test_5(self):
#         self.assertEquals(arabic_to_roman(5), "V")
#
#     def test_10(self):
#         self.assertEquals(arabic_to_roman(10), "X")
#
#     def test_50(self):
#         self.assertEquals(arabic_to_roman(50), "L")
#
#     def test_100(self):
#         self.assertEquals(arabic_to_roman(100), "C")
#
#     def test_500(self):
#         self.assertEquals(arabic_to_roman(500), "D")
#
#     def test_1000(self):
#         self.assertEquals(arabic_to_roman(1000), "M")
#
#     def test_4(self):
#         self.assertEquals(arabic_to_roman(4), "IV")
#
#     def test_9(self):
#         self.assertEquals(arabic_to_roman(9), "IX")
#
#     def test_40(self):
#         self.assertEquals(arabic_to_roman(40), "XL")
#
#     def test_90(self):
#         self.assertEquals(arabic_to_roman(90), "XC")
#
#     def test_400(self):
#         self.assertEquals(arabic_to_roman(400), "CD")
#
#     def test_900(self):
#         self.assertEquals(arabic_to_roman(900), "CM")
#
#     def test_max_roman_numeral(self):
#         self.assertEquals(arabic_to_roman(3899), "MMMDCCCXCIX")
#
#     def test_longest_roman_numeral(self):
#         self.assertEquals(arabic_to_roman(2888), "MMDCCCLXXXVIII")
#
#     def test_zero(self):
#         self.assertEquals(arabic_to_roman(0), "")
#
#     def test_negative(self):
#         self.assertEquals(arabic_to_roman(-1), "")
#
#     def test_above_max(self):
#         self.assertEquals(arabic_to_roman(3900), "")
