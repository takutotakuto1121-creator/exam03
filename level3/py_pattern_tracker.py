# py_pattern_tracker

# Assignment
# Write a function that counts the number of valid consecutive digit pairs
# in a string. A valid pair consists of two adjacent digits where the
# second digit is exactly one greater than the first. A '9' followed by a
# '0' is NOT a valid pair (no wraparound).

# Function signature
# def pattern_tracker(text: str) -> int:

# Examples
# Input
# pattern_tracker("123")
# Output
# 2
# Input
# pattern_tracker("12a34")
# Output
# 2
# Input
# pattern_tracker("987654321")
# Output
# 0
# Input
# pattern_tracker("01234567")
# Output
# 7
# Input
# pattern_tracker("abc")
# Output
# 0
# Input
# pattern_tracker("1a2b3c4")
# Output
# 0
# Input
# pattern_tracker("112233")
# Output
# 2

# Similar to (probably): No clear direct LeetCode equivalent found; this is
# a simple adjacent-pair scan with no strong single canonical match.

def pattern_tracker(text: str) -> int:
    if len(text) < 2:
        return 0

    count = 0
    for i in range(len(text) - 1):
        c1 = text[i]
        c2 = text[i + 1]
        if c1.isdigit() and c2.isdigit():
            if int(c1) + 1 == int(c2):
                count += 1

    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))
    