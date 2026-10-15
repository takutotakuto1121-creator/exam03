# py_bracket_validator

# Assignment
# Write a function that checks if the brackets in a string are valid.
# A string is valid if every opening bracket has a matching closing
# bracket in the correct order. Allowed brackets: (), [], {}. Any other
# character is ignored.

# Function signature
# def bracket_validator(s: str) -> bool:

# Examples
# Input
# bracket_validator("()")
# Output
# True
# Input
# bracket_validator("()[]{}")
# Output
# True
# Input
# bracket_validator("(]")
# Output
# False
# Input
# bracket_validator("([)]")
# Output
# False
# Input
# bracket_validator("{[]}")
# Output
# True
# Input
# bracket_validator("hello(world)")
# Output
# True
# Input
# bracket_validator("((())")
# Output
# False
# Input
# bracket_validator("")
# Output
# True

# Similar to (probably): LeetCode 20. Valid Parentheses (identical
# problem).
# Reference: question/leetcode/lc020_valid_parentheses.txt

def bracket_validator(s: str) -> bool:
    count1 = 0
    count2 = 0
    count3 = 0

    for c in s:
        if c == "(":
            count1 += 1
        elif c == ")":
            count1 -= 1
        elif c == "{":
            count2 += 1
        elif c == "}":
            count2 -= 1
        elif c == "[":
            count3 += 1
        elif c == "]":
            count3 -= 1
        else:
            pass

    if count1 == 0 and count2 == 0 and count3 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)"))
    print(bracket_validator("((())"))
    print(bracket_validator(""))