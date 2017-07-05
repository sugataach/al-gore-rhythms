'''
Determine if a a string has all unique characters, without using an additional data structure.
'''

def str_check(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return False
    return True

print(str_check('cat') == True)
print(str_check('bb') == False)
print(str_check('catc') == False)
