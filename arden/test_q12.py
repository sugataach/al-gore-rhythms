'''
Given an input string, reverse all the words.

To clarify,

input: “Interviews are awesome!”
output: “awesome! are Interviews”

Consider all consecutive non-whitespace characters as individual words. If there are multiple spaces between words reduce them to a single white space.

Also remove all leading and trailing whitespaces.
So, the output for ”   CS degree”, “CS    degree”, “CS degree   “, or ”   CS   degree   ” are all the same: “degree CS”.

Approach:
Use 2 pointers, and swap all characters in the string
Now that all words are reversed, need to go through each word and swap chars within word

O(n)
'''
import pytest

def _reverse_string(string, start, stop):
    while start < stop:
        string[start], string[stop] = string[stop], string[start]
        start += 1
        stop -= 1

def reverse_string(string):
    # reverse complete string
    _reverse_string(string, 0, len(string)-1)
    pt1 = 0
    pt2 = 0
    for char in enumerate(string):
        if char[1] == ' ':
            # stop
            _reverse_string(string, pt2, pt1-1)
            pt2 = pt1+1
        pt1 += 1
    _reverse_string(string, pt2, len(string)-1)
    return ''.join(string)

def test_reverse_string():
    string = 'perfect makes practice'
    string_list = list(string)
    result = 'practice makes perfect'
    assert reverse_string(string_list) == result

    string = '          CS degree'
    string_list = list(string.strip())
    result = 'degree CS'
    assert reverse_string(string_list) == result

    string = 'Interviews are awesome!'
    string_list = list(string)
    result = 'awesome! are Interviews'
    assert reverse_string(string_list) == result

    string = 'I am bad.'
    string_list = list(string)
    result = 'bad. am I'
    assert reverse_string(string_list) == result
