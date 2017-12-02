# def majority(arr):
#     result, count = 0, 0
#     for val in enumerate(arr):
#         if count is 0:
#             result = val[1]
#             count = 1
#         elif result == val[1]:
#             count += 1
#         else:
#             count -= 1
#     return result
#
# print(majority([1,2,3,3,3]))
# print(majority([3,3,3,2,1]))


def group_anagrams(arr):
    d = collections.defaultdict(list)
    for val in arr:
        d[''.join(sorted(val))].append(val)
    return list(d.values())

def test_group_anagrams():
    inpt = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = [["eat","tea","tea"], ["nat","tan"], ["bat"]]
    assert unknown_array_search(inpt) == result
