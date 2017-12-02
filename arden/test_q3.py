'''
Given an array of integers (positive and negative) find the largest continuous sum.

Approach:

currentSum and maxSum initialized to be the

'''
import pytest

def continuous_sum(arr):
    if len(arr) == 0:
        return 0

    current_sum = max_sum = arr[0]

    for val in arr[1:]:
        current_sum = max(current_sum + val, val)
        max_sum = max(current_sum, max_sum)
    return max_sum

def continuous_sum2(arr):
    '''return the starting and ending index of the subarray'''
    if len(arr) == 0:
        return (0,0,0)

    start = 0
    end = 0
    max_sum = current_sum = arr[0]

    for val in enumerate(arr[1:]):
        if current_sum+val[1] < val[1]:
            start = val[0]+1
        current_sum = max(current_sum+val[1], val[1])

        if current_sum > max_sum:
            end = val[0]+1
        max_sum = max(current_sum, max_sum)
    return (max_sum, start, end)

def test_continuous_sum():
    arr = [1,2,3]
    assert continuous_sum(arr) == 6
    assert continuous_sum2(arr) == (6,0,2)

    arr = []
    assert continuous_sum(arr) == 0
    assert continuous_sum2(arr) == (0,0,0)

    arr = [1,2,-1]
    assert continuous_sum(arr) == 3
    assert continuous_sum2(arr) == (3,0,1)

    arr = [1,2,-1,10]
    assert continuous_sum(arr) == 12
    assert continuous_sum2(arr) == (12,0,3)

    arr = [-40,1,40,-50,1,50,-20,1,20,0,0]
    assert continuous_sum(arr) == 52
    assert continuous_sum2(arr) == (52,4,8)

    arr = [5, 7, -13, 10, 5]
    assert continuous_sum(arr) == 15
    assert continuous_sum2(arr) == (15,3,4)
