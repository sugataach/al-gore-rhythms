'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letter (like a telephone) is given.

Approach:

Initialize an empty string as a prefix in the result array
Iterate through the letters of the input number
For each number get the letters associated with the number
For each prefix in the result set (starting with the empty string)
    - initialize a temp holder array
    - iterate through the letter mappings and add the combination of the prefix and letter mapping to the temp holder array
    - mutate the result to be the updated value of the temp holder array (this way the prefix set continues growing proportional to the input string)

Space -> O(4^n) (n being the number of digits in input string, 4 being the longest character set i.e. 7)

'''
import pytest

def letter_combo(str_digit):
    digit_map = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }

    result = ['']
    for digit in str_digit:
        letters = digit_map.get(digit,digit)
        temp = []
        for prefix in result:
            for letter in letters:
                temp.append(prefix+letter)
            result = temp
    return result

def test_letter_combo():
    assert letter_combo('2') == ['a', 'b', 'c']
    assert letter_combo('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert letter_combo('32') == ['da','db','dc','ea','eb','ec','fa','fb','fc']
