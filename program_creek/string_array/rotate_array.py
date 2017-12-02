def rotate(arr, k):
    # k = k % len(arr)
    print(arr[-k:] + arr[:-k])
    return arr[-k:] + arr[:-k]

assert(rotate([1,2,3], 2)==[2,3,1])
assert(rotate([1,2,3], 4)==[3,1,2])
assert(rotate([1,2], 1)==[2,1])
assert(rotate([1], 9)==[1])
assert(rotate([1,2,3,5], 2)==[3,5,1,2])
assert(rotate([1,2], 3)==[2,1])
