'''
Given a source word, target word and an English dictionary, transform the source word to target by changing/adding/removing 1 character at a time, while all intermediate words being valid English words. Return the transformation chain which has the smallest number of intermediate words.

Approach:

Generate graph
Iterate through graph via BFS


'''
import pytest
import collections
import string

def preprocess_dictionary(dictionary):
    graph = collections.defaultdict(list)
    letters = string.ascii_lowercase

    for word in dictionary:
        for i in range(len(word)):
            # remove a char
            remove = word[:i] + word[i+1:]
            if remove in dictionary:
                graph[word].append(remove)
            # change a char
            for char in letters:
                change = word[:i] + char + word[i+1:]
                if change in dictionary and change != word:
                    graph[word].append(change)
        # add a char
        for i in range(len(word)+1):
            for char in letters:
                add = word[:i] + char + word[i:]
                if add in dictionary:
                    graph[word].append(add)
    return graph

def transform_word(source_word, target_word, dictionary):
    graph = preprocess_dictionary(dictionary)
    paths = collections.deque([ [source_word] ])
    extended = set()
    # print(graph)
    while len(paths) != 0:
        # print(paths)
        current_path = paths.popleft()
        current_word = current_path[-1]
        if current_word == target_word:
            return current_path
        elif current_word in extended:
            continue

        extended.add(current_word)
        transforms = graph[current_word]
        for word in transforms:
            if word not in current_path:
                paths.append(current_path[:]+[word])
    return []

def test_transform_word():
    dictionary = ['cat', 'bat', 'mat', 'sat', 'at', 'ate']
    assert(transform_word('cat', 'ate', dictionary)) == ['cat','at','ate']
