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
        Tuple containing all ordered subtractive combination pairs found and the respective index at which they start
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

        if leading_numeral == "I" and second_numeral in ("V", "X"):
            continue
        elif leading_numeral == "X" and second_numeral in ("L", "C"):
            continue
        elif leading_numeral == "C" and second_numeral in ("D", "M"):
            continue
        else:
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

    ivxlcdm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ivxlcdm_order = ["I", "V", "X", "L", "C", "D", "M"]

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

            subtractive_combinations_indexes = [i[1] for i in subtractive_combination_pairs]
            last_roman_numeral = "M"  # Max char (first case always goes through)
            jump_char = False  # Jump over the 2nd char of a subtractive combination pair
            count = 0

            arabic_numeral = 0
            for char in roman_numeral:

                # When a subtractive combination is found, do not check descending order for the 2nd value in the pair
                if not jump_char:
                    # If char is bigger than the last char, roman numeral is wrong
                    if char not in ivxlcdm_order[:ivxlcdm_order.index(last_roman_numeral) + 1]:  # char <= previous_char
                        return -1

                    # Last char is only kept if this char was not part of a subtractive combination
                    last_roman_numeral = char
                else:
                    jump_char = False

                # If value is the 1st of a subtractive combination, subtract its value, sum it otherwise
                if count in subtractive_combinations_indexes:
                    arabic_numeral -= ivxlcdm[char]
                    jump_char = True
                else:
                    arabic_numeral += ivxlcdm[char]

                count += 1

            return arabic_numeral

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
    #   max value = 3899 (classic representation)
    # convert into Roman

    return ""
