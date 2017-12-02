'''
Given a string of opening and closing parentheses, check whether it’s balanced.

We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.

Assume that the string doesn’t contain any other character than these, no spaces words or numbers.

Balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]‘ is not.

Approach:

Have a dictionary mapping closing brackets to opening brackets
Keep a stack that you push opening brackets onto
Iterate through string
When you encounter a closing bracket, pop from the stack
    - IF there's nothing to pop
        - return False
    - check if they match
        - IF NOT -> Return False

At the end of the string, return whether the stack is empty

O(n) -> space
O(n) -> time

'''
import pytest

def balanced_parentheses(string):
    bracket_dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    opening_bracket_stack = []
    for char in string:
        if char in bracket_dict.values():
            opening_bracket_stack.append(char)
        else:
            try:
                opener = opening_bracket_stack.pop()
                if opener != bracket_dict[char]:
                    return False
            except:
                return False
    return len(opening_bracket_stack) == 0


def test_balanced_parentheses():
    string = "[{}]"
    assert(balanced_parentheses(string)) == True

    string = "[{]"
    assert(balanced_parentheses(string)) == False

    string = "[{[{}]}])"
    assert(balanced_parentheses(string)) == False

    string = "[{[{}]}]((((((((((()))))))))))"
    assert(balanced_parentheses(string)) == True

    string = "[{[{}]}]((((((((((("
    assert(balanced_parentheses(string)) == False

    string = "[]()"
    assert(balanced_parentheses(string)) == True
