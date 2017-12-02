'''
Given an integer array, output all pairs that sum up to a specific value k.
'''
import pytest

def pair_sum(arr, k):
    seen = set()
    result = []
    for val in arr:
        target = k - val
        if target in seen:
            result.append((min(val,target), max(val,target)))
            seen.remove(target)
        else:
            seen.add(val)
    return result

def test_pair_sum():
    arr = [1,2,3]
    k = 3
    assert pair_sum(arr, k) == [(1,2)]

    arr = [1,2,2,3]
    k = 3
    assert pair_sum(arr, k) == [(1,2)]

    arr = [1,2,3]
    k = 6
    assert pair_sum(arr, k) == []

    arr = []
    k = 3
    assert pair_sum(arr, k) == []
