# py_anagram

# Assignment
# Write a function that checks if two strings are anagrams. They must
# contain exactly the same letters with the same quantity, ignoring case
# and spaces.

# Function signature
# def anagram(s1: str, s2: str) -> bool:

# Examples
# Input
# anagram("listen", "silent")
# Output
# True
# Input
# anagram("Triangle", "Integral")
# Output
# True
# Input
# anagram("Dormitory", "Dirty Room")
# Output
# True
# Input
# anagram("hello", "world")
# Output
# False
# Input
# anagram("", "")
# Output
# True
# Input
# anagram("abc", "abcc")
# Output
# False

# Similar to (probably): LeetCode 242. Valid Anagram (identical idea; here
# case and spaces are also normalized away before comparing).
# Reference: question/leetcode/lc242_valid_anagram.txt

def anagram(s1: str, s2: str) -> bool:
    cleaned_s1 = s1.replace(" ", "").lower()
    cleaned_s2 = s2.replace(" ", "").lower()
    if len(cleaned_s1) != len(cleaned_s2):
        return False

    counts = {}
    for c in cleaned_s1:
        counts[c] = counts.get(c, 0) + 1

    for c in cleaned_s2:
        if c not in counts:
            return False
        counts[c] -= 1
        if counts[c] < 0:
            return False

    for v in counts.values():
        if v != 0:
            return False

    return True


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))