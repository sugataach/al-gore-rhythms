'''
Flatten a dictionary, array
'''
import pytest

def flatten_dict(dictionary, parent_key=''):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + '.' + key if parent_key else key
        if type(value) == dict:
            items.extend(flatten_dict(value, new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)

def flatten_array(arr):
    items = []
    for val in arr:
        if type(val) == list:
            items.extend(flatten_array(val))
        else:
            items.append(val)
    return items

def test_flatten_dict():
    dictionary = {
        '1' : {
            'a' : '2',
            'b' : '3'
        },
        '2' : '4'
    }
    result = {
        '1.a' : '2',
        '1.b' : '3',
        '2' : '4'
    }
    assert flatten_dict(dictionary) == result

def test_flatten_array():
    arr = [1,[2,[3,[4]]]]
    result = [1,2,3,4]
    assert flatten_array(arr) == result
