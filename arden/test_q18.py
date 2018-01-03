'''
Given an integer array, one element occurs even number of times and all others have odd occurrences. Find the element with even occurrences.

Approach:
Iterate through the array and store the counts of each element in a hash table
Iterate through the hash table and return the count that is even (i.e. count%2 = 0)

Space -> O(N)
Time -> O(N)
'''
import pytest
import collections

def even_num(arr):
    d = collections.defaultdict(int)
    for elem in arr:
        d[elem] += 1
    for key,val in d.items():
        if val%2 == 0:
            return key
    return -1

def test_even_num():
    arr = [1,2,2,2,3,3,3,4,4]
    assert even_num(arr) == 4

    arr = [1,2,2,2,3,3,3,4,4,4]
    assert even_num(arr) == -1
