"""
Implement randomized quicksort.

Time: O(n*log(n)) (average time, after choosing a random pivot, can degrade to O(n^2))
Space: O(1) -> in-place
"""
from random import randint

def partition(arr, left, right):
    pivot = randint(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]
    i = left + 1
    pivot = arr[left]
    for j in range(left+1, right+1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    pos = i-1
    arr[left], arr[pos] = arr[pos], arr[left]
    return pos

def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    def _quicksort(arr, left, right):
        if left >= right:
            return
        pivot = partition(arr, left, right)
        _quicksort(arr, left, pivot-1)
        _quicksort(arr, pivot+1, right)
    return _quicksort(arr, left, right)

a = [1,4,4,2,5,7]
sorted_a = [1,2,4,4,5,7]
quicksort(a)
print(a == sorted_a)
