'''
Given two strings, check if they’re anagrams or not. Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation and capitalization. Each letter should have the same count in both strings.

For example, ‘Eleven plus two’ and ‘Twelve plus one’ are meaningful anagrams of each other.

Approach:
Initialize a dictionary
Iterate through string1
    - If char.lower() in ascii_lowercase
        - add count to dictionary
Iterate through string2
    - If char.lower() is in ascii_lowercase
        - decrement the count in dictionary
        - check if the count is < 0 -> return False
Iterate through dictionary:
    - If there are any count > 0, return False
Return True


O(n) -> space
O(n) -> time

'''
import pytest
import collections
import string

def is_anagram(string1, string2):
    d = collections.defaultdict(int)
    for char in string1:
        if char.lower() in string.ascii_lowercase:
            d[char.lower()] += 1
    for char in string2:
        if char.lower() in string.ascii_lowercase:
            d[char.lower()] -= 1
            if d[char.lower()] < 0:
                return False
    for value in d.values():
        if value > 0:
            return False
    return True

def test_unique_string():
    string1 = 'Eleven plus two'
    string2 = 'Twelve plus one'
    assert is_anagram(string1, string2) == True

    string1 = 'Eleven plus twoo'
    string2 = 'Twelve plus one'
    assert is_anagram(string1, string2) == False

    string1 = 'Eleven plus two.'
    string2 = 'Twelve plus one'
    assert is_anagram(string1, string2) == True

    string1 = ''
    string2 = ''
    assert is_anagram(string1, string2) == True
