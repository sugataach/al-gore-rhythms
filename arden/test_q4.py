'''
There is an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Approach A:

iterate through the array, keeping track of the count of all numbers in a hash
iterate thorugh the 2nd array, subtracting the count from hash
iterate through the hash and look for a count which is 1

Approach B:

sum all elements in arr1
subtract from sum of all elements in arr2
'''
import pytest
import collections

def missing(arr, arr2):
    if len(arr) == len(arr2):
        return 0

    result = []
    d = collections.defaultdict(int)

    # build dict
    for item in arr2:
        d[item] += 1

    # check for missing values
    for item in arr:
        d[item] -= 1
        if d[item] < 0:
            return item
    return 0

def missing2(arr, arr2):
    if len(arr) == len(arr2):
        return 0
    return sum(arr) - sum(arr2)

def test_missing():
    import random

    arr = [1,2,3]
    arr2 = [1,2,3]
    random.shuffle(arr2)
    assert missing(arr, arr2) == 0
    assert missing2(arr, arr2) == 0

    arr = [1,2,3]
    arr2 = [1,2]
    random.shuffle(arr2)
    assert missing(arr, arr2) == 3
    assert missing2(arr, arr2) == 3

    arr = [1,2,3,3,3,3]
    arr2 = [1,2,3,3,3]
    random.shuffle(arr2)
    assert missing(arr, arr2) == 3
    assert missing2(arr, arr2) == 3

    arr = [1,5,2,3,5,10,23,-9]
    arr2 = [1,5,2,3,10,23,-9]
    random.shuffle(arr2)
    assert missing(arr, arr2) == 5
    assert missing2(arr, arr2) == 5
