"""
Implement randomized quicksort.

Time: O(n*log(n)) (average time, after choosing a random pivot, can degrade to O(n^2))
Space: O(1) -> in-place
"""
from random import randint

def partition(arr, left, right, pivot_index):
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    pivot = arr[right]
    swap_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
            swap_index += 1
    arr[right], arr[swap_index] = arr[swap_index], arr[right]
    return swap_index

def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    def _quicksort(arr, left, right):
        if left >= right:
            return
        pivot_index = randint(left,right)
        pivot = partition(arr, left, right, pivot_index)
        _quicksort(arr, left, pivot-1)
        _quicksort(arr, pivot+1, right)
    return _quicksort(arr, left, right)

a = [7,4,4,2,5,1]
sorted_a = [1,2,4,4,5,7]
quicksort(a)
print(a == sorted_a)

# a = [3, 1, 2]
# print(quicksort(a))
# print(a)
