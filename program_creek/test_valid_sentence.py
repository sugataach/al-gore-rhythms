'''
Given a string and a dictionary of words, determine if the string is valid based on all the dictionary words.
'''

import pytest

# memo = {}
# def _valid_sentence(s, words):
#     if s == '': return True
#     global memo
#     if s in memo: return memo[s]
#     for i in range(1,len(s)+1):
#         sub = s[:i]
#         if not sub in words: continue
#         if _valid_sentence(s[i:], words):
#             memo[s] = True#; print memo
#             return True
#     return False

def _valid_sentence(sentence, dictionary):
    segmented = [True]
    for i in range(len(sentence)):
        segmented.append(False)
        for j in range(i, -1, -1):
            if segmented[j] and sentence[j:i+1] in dictionary:
                segmented[i+1] = True
                break
    return segmented[len(sentence)]

def valid_sentence(sentence, dictionary):
    string_array = sentence.split()
    for val in string_array:
        string = val.lower().strip('.,!')
        if string not in dictionary:
            if not _valid_sentence(string, dictionary):
                return False
    return True

def test_valid_sentence():
    string = 'Practice makes perfect.'
    dictionary = ['practice', 'perfect', 'makes']
    assert valid_sentence(string, dictionary) == True

    string = 'Practice makes perfect.'
    dictionary = ['practice', 'perfect']
    assert valid_sentence(string, dictionary) == False

    string = 'practicemakesxperfect'
    dictionary = ['practice', 'perfect', 'makes', 'xp', 'xperfect']
    assert valid_sentence(string, dictionary) == True
