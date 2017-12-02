'''
Generate all permutations of a given string.

Approach:

melt string into len of 1
after breaking down the string (of length N-1)
iterate through the permutations
iterate through the chars in a given permutation
insert the element to get a new permuation and add to the result
return result

'''
import pytest

def permutations(string):
    if len(string) <= 1:
        return [string]
    perms = permutations(string[1:])
    char = string[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

def test_permutations():
    result = ['abe','bae','bea','aeb','eab','eba']
    assert permutations('abe') == result
