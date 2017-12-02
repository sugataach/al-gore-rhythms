'''
We are given 3 strings: str1, str2, and str3.

Str3 is said to be a shuffle of str1 and str2 if it can be formed by interleaving the characters of str1 and str2 in a way that maintains the left to right ordering of the characters from each string.

For example, given str1=”abc” and str2=”def”, str3=”dabecf” is a valid shuffle since it preserves the character ordering of the two strings.

So, given these 3 strings write a function that detects whether str3 is a valid shuffle of str1 and str2.

Approach:

2 pointers, 1 on str1 and 1 on str2
As we iterate through str3, the char must be either str1[pointer] or str2[pointer]
If it isn't -> return False
When we hit the end of str3, we must also hit the end of str1 and str2

'''
import pytest

def interleaved(str1, str2, str3, cache=set()):
    if (str1, str2) in cache:
        return False

    # check if the strings are valid
    if len(str1)+len(str2) != len(str3):
        return False

    # if at the end of any string
    # check if the remaining string matches up
    if not str1 or not str2 or not str3:
        if str1+str2 == str3:
            return True
        else:
            return False

    if str1[0] != str3[0] and str2[0] != str3[0]:
        return False

    if str1[0] == str3[0] and interleaved(str1[1:], str2, str3[1:]):
        return True
    if str2[0] == str3[0] and interleaved(str1, str2[1:], str3[1:]):
        return True

    cache.add((str1, str2))

    return False


def interleaved_iterative(str1, str2, str3):
    '''
    Currently this code does not work
    '''
    if len(str3) == 0 or len(str3) < len(str1)+len(str2):
        return False
    ptr1, ptr2 = 0, 0
    for val in enumerate(str3):
        idx = val[0]
        char = val[1]
        print(ptr1, ptr2)
        if char == str1[ptr1] and char == str2[ptr2]:
            ########### NOT WORKING #############
            get_correct_pointer(str1[ptr1:], str2[ptr2:], str3[idx:])
        elif char == str1[ptr1]:
            if ptr1 < len(str1)-1:
                ptr1 += 1
        elif char == str2[ptr2]:
            if ptr2 < len(str2)-1:
                ptr2 += 1
        else:
            return False
    return ptr1 == len(str1)-1 and ptr2 == len(str2)-1

def get_correct_pointer(str1, str2, str3):
    pass

def test_interleaved():
    str1 = 'abc'
    str2 = 'def'
    str3 = 'dabecf'
    assert interleaved(str1, str2, str3) == True

    str1 = 'abb'
    str2 = 'bbc'
    str3 = 'abbbbc'
    assert interleaved(str1, str2, str3) == True
