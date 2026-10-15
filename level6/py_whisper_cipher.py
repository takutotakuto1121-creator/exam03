# py_whisper_cipher

# Assignment
# Write a function that applies a Caesar cipher by shifting letters in a
# string by a given amount. Non-alphabetic characters remain unchanged.
# The shift can be negative (shift left) and case is preserved.

# Function signature
# def whisper_cipher(text: str, shift: int) -> str:

# Examples
# Input
# whisper_cipher("hello", 3)
# Output
# "khoor"
# Input
# whisper_cipher("Hello World!", 1)
# Output
# "Ifmmp Xpsme!"
# Input
# whisper_cipher("xyz", 3)
# Output
# "abc"
# Input
# whisper_cipher("ABC123def", 5)
# Output
# "FGH123ijk"
# Input
# whisper_cipher("", 10)
# Output
# ""
# Input
# whisper_cipher("abc", -3)
# Output
# "xyz"

# Similar to (probably): No single canonical LeetCode problem for a
# generic Caesar cipher; conceptually related to character-shift problems
# such as LeetCode 2325. Decode the Message.

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if c.isalpha() and c.upper() == c:
            result += chr(ord('A') + (ord(c) - ord('A') + shift) % 26)
        elif c.isalpha() and c.lower() == c:
            result += chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
        else:
            result += c
    return result


if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))