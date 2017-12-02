'''
Binary search works on sorted arrays, it will search for a given element and return it's index or -1 if not found.

O(logN) -> Time
O(1) -> Space
'''

def binary_search(arr, k):
    min_value = 0
    max_value = len(arr)-1
    while True:
        if min_value > max_value:
            return -1
        mid = (min_value + max_value) // 2
        if arr[mid] > k:
            max_value = mid - 1
        elif arr[mid] < k:
            min_value = mid + 1
        else:
            return mid

def binary_search_recursive(arr, k):
    def recurse(min_value, max_value):
        mid = (min_value + max_value) // 2
        if min_value > max_value:
            return -1
        elif arr[mid] > k:
            return recurse(min_value, mid-1)
        elif arr[mid] < k:
            return recurse(mid+1, max_value)
        else:
            return mid
    return recurse(0, len(arr)-1)

arr = [1,2,3,4,5]
k = 5
k2 = 0

print(binary_search(arr, k) == 4)
print(binary_search_recursive(arr, k) == 4)

print(binary_search(arr, k2) == -1)
print(binary_search_recursive(arr, k2) == -1)
