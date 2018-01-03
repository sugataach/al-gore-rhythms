'''
Given a sorted array of unknown length and a number to search for, return the index of the number in the array. Accessing an element out of bounds throws exception. If the number occurs multiple times, return the index of any occurrence. If it isn’t present, return -1.

Approach:

Search through the array for values greater than k or an IndexError
Iterate while arr[i] < k and increment i from 0 to 2^i
This way you know your right side max

Perform a binary search between arr[2^(i-1) + 1] and arr[2^(i) - 1]
Anytime the right side runs into an IndexError -> right = mid-1

O(1) -> space
O(logN) -> time

'''
import pytest
import collections

def unknown_array_search(arr, k):
    i = 0
    idx = 2**i
    while True:
        try:
            if arr[idx] == k:
                return i
            if arr[idx] > k:
                break
            i += 1
            idx = 2**i
        except:
            break

    left = (2**(i-1)) + 1
    right = (2**i) - 1

    while True:
        try:
            if left > right:
                return -1

            mid = (left+right)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        except:
            right = mid - 1
    return -1


def test_unknown_array_search():
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 8
    assert unknown_array_search(arr, k) == 7

    arr = [1,2,3,4,5]
    k = 6
    assert unknown_array_search(arr, k) == -1
