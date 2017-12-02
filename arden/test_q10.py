'''
Given an array of integers find the kth element in the sorted order (not the kth distinct element).

So, if the array is [3, 1, 2, 1, 4] and k is 3 then the result is 2, because it’s the 3rd element in sorted order (but the 3rd distinct element is 3).

Approach A:
Sort and count -> O(n*logn)

Approach B:
Quicksort selection method
Choose pivot
Sort until kth element found
| O(nlogn) -> average, O(n^2) -> worst case (if you choose the wrong pivot) |
'''
import pytest
from random import randint

def partition(arr, left, right, pivot_index):
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    swap_index = left
    pivot = arr[right]
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    arr[swap_index], arr[right] = arr[right], arr[swap_index]
    return swap_index

def convert_array(arr, k):
    left = 0
    right = len(arr) - 1
    def _convert_array(arr, left, right, k):
        if not 1 < k < len(arr):
            return
        if left == right:
            return arr[left]

        while True:
            # divide array into 2 subarrays
            pivot_random_index = randint(left,right)
            pivot_index = partition(arr, left, right, pivot_random_index)

            # we know that the pivot_index is in the right place now
            # get the rank by subtracting all the element less than it and then adding 1
            rank = pivot_index - left + 1
            if rank == k:
                return arr[pivot_index]
            elif k < rank:
                # if k is smaller than the index, look in the left subarray
                return _convert_array(arr, left, pivot_index-1, k)
            else:
                # if k is greater than the index, look in the right subarray
                # k gets adjusted for the smaller subarray
                return _convert_array(arr, pivot_index+1, right, k-rank)
    return _convert_array(arr, left, right, k)


def test_convert_array():
    arr = [3,1,2,1,4]
    k = 3
    assert convert_array(arr, k) == 2
