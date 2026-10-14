# py_echo_validator

# Assignment
# Write a function that checks if a string is a palindrome, ignoring
# spaces/punctuation and case. Only alphabetic characters are considered
# for the comparison.

# Function signature
# def echo_validator(text: str) -> bool:

# Examples
# Input
# echo_validator("racecar")
# Output
# True
# Input
# echo_validator("A man a plan a canal Panama")
# Output
# True
# Input
# echo_validator("race a car")
# Output
# False
# Input
# echo_validator("Was it a car or a cat I saw")
# Output
# True
# Input
# echo_validator("hello")
# Output
# False
# Input
# echo_validator("Madam Im Adam")
# Output
# True
# Input
# echo_validator("")
# Output
# False

# Similar to (probably): LeetCode 125. Valid Palindrome (exact same idea:
# lowercase + keep only alphanumeric/alphabetic characters, then check
# palindrome).
# Reference: question/leetcode/lc125_valid_palindrome.txt

import string


def clean_string(text: str) -> str:
    spaces = " \t\n\v\f\r"  # man isspace
    spaces += string.punctuation
    cleaned_text = ""

    for c in text:
        if c in spaces:
            pass
        else:
            cleaned_text += c.lower()

    return cleaned_text


def reverse_string(string: str) -> str:
    reverse = ""
    for i in range(len(string) -1 , -1, -1):
        reverse += string[i]
    return reverse


def echo_validator(text: str) -> bool:
    if not text:
        return False

    clean_text = clean_string(text)
    reverse_text = reverse_string(clean_text)

    if clean_text == reverse_text:
        return True
    else:
        return False


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))