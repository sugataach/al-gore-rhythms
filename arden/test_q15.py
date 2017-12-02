'''
Find the first non-repeated (unique) character in a given string.

Basically, this means that there are multiple characters that are repeated, your job is to find the character that only occurs once in the string.

Approach:

Keep a hash table of the character and their count
Iterate through the string, incrementing the count
When you reach the end, iterate through the dictionary, looking for a count of 1
If there is one, return the char

O(n) -> space
O(n) -> time

'''
import pytest
import collections

def unique_string(string):
    d = collections.defaultdict(int)
    for char in string:
        d[char] += 1
    for key in d.keys():
        if d[key] == 1:
            return key
    return False

def test_unique_string():
    string = "aaaaaaabcc"
    assert(unique_string(string)) == 'b'

    string = "aaaaaaa"
    assert(unique_string(string)) == False
