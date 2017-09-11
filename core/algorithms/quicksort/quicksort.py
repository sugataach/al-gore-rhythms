"""
Implement randomized quicksort.

Time: O(n*log(n)) (average time, after choosing a random pivot, can degrade to O(n^2))
Space: O(1) -> in-place
"""
from random import randint

def partition(arr, left, right):
    # if you're using a random pivot, you'll need to swap the left most value and the pivot
    # otherwise ignore the next 2 lines and just choose the pivot to be the left most value
    # has performance implications obviously
    pivot = randint(left, right) # choose a random pivot
    arr[left], arr[pivot] = arr[pivot], arr[left] # swap left and pivot

    i = left + 1 # i pointer is to next element from the left
    pivot = arr[left] # pivot is the left most element
    for j in range(left+1, right+1): # iterate from i to right (remember python value on right of range is non-inclusive)
        if arr[j] < pivot: # if j < i -> swap, increment i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    pos = i-1 # at the very end swap the value of i-1 with the pivot, so the pivot is in the middle now
    arr[left], arr[pos] = arr[pos], arr[left]
    return pos # return the pivot

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

a = [7,4,4,2,5,1]
sorted_a = [1,2,4,4,5,7]
quicksort(a)
print(a == sorted_a)
