#!python2
# coding: utf-8

"""
ROMAN NUMERALS CONVERTER
Converts Roman Numerals into Arabic Numerals (and vice versa)

DEPENDENCIES:
    - Python 2.7

HOW TO RUN:
    - TODO
"""

import re

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1.dev'
__date__ = '22:31h, 17/12/2017'
__status__ = 'Production'


def is_possible_roman_numeral(string):
    """
    True if string is a possible Roman Numeral, False otherwise.
    Checks if only a combination of the following characters exist (ignoring case): IVXLCDM
    Does not verify if it is a valid Roman Numeral.

    PARAMETERS:
        string : str

    RETURNS: bool
    """
    if 0 < len(string) <= 14:  # Longest Roman numeral (2888) has 14 characters
        # Matches strings that consist of IVXLCDM characters starting at index 0 (ignoring case)
        # If this happens, returns True if the whole string was matched, False otherwise
        match = re.match("[IVXLCDM]+", string, flags=re.IGNORECASE)
        if match:
            return len(match.group()) == len(string)
    
    return False


def is_non_zero_arabic_numeral(string):
    """
    True if string is a non zero natural Arabic Numeral less than or equal to 3899 (max Roman Numeral), False otherwise.

    PARAMETERS:
        string : str

    RETURNS: bool
    """
    # Is comprised only of digits and is not only zero(es)
    return string.isdigit() and int(string) != 0 and int(string) <= 3899


def at_most_once_vld(string):
    """
    True if string contains zero or only one instance of each VLD characters, False otherwise.

    PARAMETERS:
        string : str

    RETURNS: bool
    """
    vld = {"V": 0, "L": 0, "D": 0}

    for letter in string.upper():
        if letter in vld:
            # Count occurrences of letter
            # If any of those counts reaches 2, returns False. True otherwise
            vld[letter] += 1
            if vld[letter] > 1:
                return False
    
    return True


def at_most_3_in_row_ixcm(string):
    """
    True if IXCM do not occur more than 3 times in a row, False otherwise.

    PARAMETERS:
        string : str

    RETURNS: bool
    """
    ixcm = ("I", "X", "C", "M")
    
    current_letter = ""
    letter_count = 0

    for letter in string.upper():
        if letter in ixcm:
            # Count sequential occurrences
            # If any of those counts reaches 4, returns False. True otherwise
            if letter != current_letter:
                current_letter = letter
                letter_count = 1
            else:
                letter_count += 1
                if letter_count > 3:
                    return False
        
        # if letter not one of IXCM, reset current_letter and count
        else:
            current_letter = ""
            letter_count = 0
    
    return True


################
# Main Functions
################


def roman_to_arabic(roman_numeral):
    """
    Converts a Roman numeral to an Arabic numeral.

    PARAMETERS:
        roman_numeral : str

    RETURNS: int
        Actual conversion to Arabic Numeral if possible, -1 otherwise.
    """
    # Check if roman_numeral is a str
    if not isinstance(roman_numeral, str):
        raise TypeError("Parameter 'roman_numeral' must be of type str")

    # VERIFY VALIDITY
    
    # is alpha string
    # only characters allowed: IVXLCDM (lower or upper case)
    # V, L and D can only appear at most once
    # I, X, C and M cannot occur more than 3 times in a row
    if (is_possible_roman_numeral(roman_numeral) and
            at_most_once_vld(roman_numeral) and
            at_most_3_in_row_ixcm(roman_numeral)):

        pass  # TODO (use string.upper)
        # Rules:
        # - Numerals arranged in descending order (except for subtractive combinations)
        # Subtractive combinations Rules:
        # - Only one I, X and C can be used as the leading numeral in a subtractive pair
        # - I can ony be placed before V and X
        # - X can only be placed before L and C
        # - C can only be placed before D and M

        # CONVERSION TO ARABIC NUMERAL

    return -1


def arabic_to_roman(arabic_numeral):  # TODO
    """
    Converts an Arabic numeral to a Roman numeral.

    PARAMETERS:
        arabic_numeral : int

    RETURNS: str
        Actual conversion to Roman Numeral if possible, empty string otherwise.
    """
    # Check if string is an int
    if not isinstance(arabic_numeral, int):
        raise TypeError("Parameter 'arabic_numeral' must be of type int")

    # verify validity of arabic_numeral
    #   only numeric characters
    #   no 0
    #   positive only
    #   max value = 3999 (classic representation)
    # convert into Roman

    return ""
