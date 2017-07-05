from collections import defaultdict

'''
Determine if a string has all unique characters.
'''

def str_check(str):
    if str is None:
        return False
    
    h = defaultdict(int)
    for char in str:
        if char in h:
            return False
        h[char] += 1
    return True

print(str_check('bb') == False)
print(str_check('cat') == True)
print(str_check('catc') == False)


