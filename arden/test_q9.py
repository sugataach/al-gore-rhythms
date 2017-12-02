'''
Given an array [a1, a2, …, aN, b1, b2, …, bN, c1, c2, …, cN]  convert it to [a1, b1, c1, a2, b2, c2, …, aN, bN, cN] in-place using constant extra space

Approach:
Iterate through the array
Get the corresponding series element as you walk through the array
Swap the element as you continue (this will result in )

'''
import pytest

def get_index(idx, N):
    return int((idx%3)*N + (idx/3))

def convert_array(arr):
    N = len(arr)/3
    for curr_idx in range(len(arr)):
        swap_idx = get_index(curr_idx, N)
        while swap_idx < curr_idx:
            swap_idx = get_index(swap_idx, N)
        arr[curr_idx], arr[swap_idx] = arr[swap_idx], arr[curr_idx]

def convert_array_extra_space(arr):
    N = len(arr)/3
    result = []
    for i in range(len(arr)):
        element_idx = get_index(i, N)
        result.append(arr[element_idx])
    return result

def test_convert_array():
    arr = [1,2,3,11,12,13,21,22,23]
    result = [1,11,21,2,12,22,3,13,23]
    convert_array(arr)
    assert(arr) == result
