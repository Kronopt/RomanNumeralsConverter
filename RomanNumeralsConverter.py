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
    Checks if only a combination of the following characters exist: IVXLCDM (upper case)
    Does not verify if it is a valid Roman Numeral.

    PARAMETERS:
        string : str

    RETURNS: bool
    """
    if 0 < len(string) <= 14:  # Longest Roman numeral (2888) has 14 characters
        # Matches strings that consist of IVXLCDM characters starting at index 0
        # If this happens, returns True if the whole string was matched, False otherwise
        match = re.match("[IVXLCDM]+", string)
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

    for letter in string:
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

    for letter in string:
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
        
        # If letter not one of IXCM, reset current_letter and count
        else:
            current_letter = ""
            letter_count = 0
    
    return True


def find_subtractive_combinations(string):
    """
    Finds subtractive combination pairs in string.

    PARAMETERS:
        string : str

    RETURNS: ( (str pair, int index), ... )
        Tuple containing all subtractive combination pairs found and the respective index at which each pair starts
    """
    ivxlcdm = ["I", "V", "X", "L", "C", "D", "M"]

    subtractive_pairs = []
    previous_char = "M"  # Max char (first case always goes through)

    count = 0
    for char in string:
        if char not in ivxlcdm[:ivxlcdm.index(previous_char) + 1]:  # char <= previous_char
            subtractive_pairs.append((previous_char + char, count-1))

        previous_char = char
        count += 1

    return tuple(subtractive_pairs)


def subtractive_combination_validity(pairs):
    """
    Checks the validity of subtractive pairs. True if all pairs are valid, False otherwise.

    PARAMETERS:
        pairs : ( (str pair, int index), ... ) output of find_subtractive_combinations()
            Tuple of upper case character pairs and index

    RETURNS: bool
    """
    for (leading_numeral, second_numeral), _ in pairs:  # Ignore index of pair in original string
        # Only one I, X and C can be used as the leading numeral in a subtractive pair
        # I can only be placed before V and X
        # X can only be placed before L and C
        # C can only be placed before D and M

        if leading_numeral == "I" and second_numeral not in ("V", "X"):
            return False
        elif leading_numeral == "X" and second_numeral not in ("L", "C"):
            return False
        elif leading_numeral == "C" and second_numeral not in ("D", "M"):
            return False

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

    roman_numeral = roman_numeral.upper()  # Ignore case

    # Is alpha string
    # Only characters allowed: IVXLCDM (lower or upper case)
    # V, L and D can only appear at most once
    # I, X, C and M cannot occur more than 3 times in a row
    if (is_possible_roman_numeral(roman_numeral) and
            at_most_once_vld(roman_numeral) and
            at_most_3_in_row_ixcm(roman_numeral)):

        # Subtractive combinations Rules:
        #   Only one I, X and C can be used as the leading numeral in a subtractive pair
        #   I can ony be placed before V and X
        #   X can only be placed before L and C
        #   C can only be placed before D and M
        subtractive_combination_pairs = find_subtractive_combinations(roman_numeral)
        if subtractive_combination_validity(subtractive_combination_pairs):
            pass

            # Numerals arranged in descending order (except for subtractive combinations) # TODO - use index in subtractive_combination_pairs

            # CONVERSION TO ARABIC NUMERAL  # TODO

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
