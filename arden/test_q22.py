'''
Given an integer array, one element occurs odd number of times and all the others have even occurences. Find the element with the odd occurences.

Approach 1:

Initialize a hash table
Iterate through the array
Store the "element" : count

Iterate through the hash table and look for count%2 == 1

Time -> O(n) + O(k) -> 2*O(n) -> O(n), at worst case, k is equal to n, average case -> k < n

Space -> O(n) + O(k) -> 2*O(n) -> O(n)

Approach 2:

XOR all the elements in array to find the odd element

Why?

XOR'ing an element with itself even number of times = element
XOR'ing an element with itself odd number of times = 0

Time -> O(n), still need to walk through the array

Space -> O(c), constant amount of memory to store the result as you walk through the array (ie. not proportional to the length of the array,)
'''
import pytest
import functools

def odd_elem(arr):
    # return functools.reduce(lambda x, y: x^y, arr)
    result = arr[0]
    for elem in arr[1:]:
        result = result^elem
    return result

def test_odd_elem():
    arr = [1,2,3,1,2,3,1]
    assert(odd_elem(arr)) == 1
