# RomanNumeralsConverter
[![Build Status](https://travis-ci.org/Kronopt/RomanNumeralsConverter.svg?branch=master)](https://travis-ci.org/Kronopt/RomanNumeralsConverter)

Convert Roman Numerals into Arabic Numerals (and vice versa)

#### Dependencies
Python 2.7

#### How to run
Through the command line, like so:

`RomanNumeralsConverter.py type numeral`

* `type` is either 'roman' or 'arabic', to explicitly define the type of numeral to convert
* `numeral` is either a Roman numeral or an Arabic numeral (both between 1 and 3899)
* `-h, --help` shows the help text

A malformed numeral will yield either `""`, for Roman numerals, or `-1`, for Arabic numerals
