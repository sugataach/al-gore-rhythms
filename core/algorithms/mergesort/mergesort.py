"""
Implement mergesort

Time: O(n*log(n))
Space: O(n)
"""

def merge(left, right):
    left_index = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = mergesort(arr[:half])
    right = mergesort(arr[half:])

    return merge(left, right)

a = [1,4,2,6,1]
print(mergesort(a) == [1,1,2,4,6])
