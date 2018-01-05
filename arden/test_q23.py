'''
Given a text file and a word, find the positions that the word occurs in the file. We'll be asked to find the positions of many words in the same file.

Approach:

Precomputation is a must because of the multiple lookup constraint
Data structure must hold a mapping of "word" : {locations of word}

Approach 1:

Preprocess the text file and store all the words and their respective positions in a hash table.
Use the hash table to perform lookups.

Time -> O(n) + O(1), n being the total number of words in the text file and O(1) being the cost of performing a lookup in a hash table

Space -> O(n), n being the number of unique words in the text file

Approach 2:

We can be much more space efficient if we use a Trie (aka Prefix Tree)

Example:

text file = subtree, subset, submit

hash table will store (7 + 6 + 6 = 19 chars)

trie will store (3 + 4 + 3 + 3 = 13 chars)

This can result in huge gains for large data sets, in terms of compression.

But also, as a hash table increases in size, there can be a higher likelihood of hash collisions, which could deteriorate the lookup time to O(n), where n is the number of keys inserted -> i.e. open addressing implementation.

Lookup in a balanced tree is O(m*log(n)), where m is the key length 

'''
import pytest

def word_positions(dictionary, word):
    pass

def test_word_positions():
    dictionary = []
    word =
    assert(odd_elem(arr)) == 1
