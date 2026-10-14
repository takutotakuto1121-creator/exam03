# py_inter

# Assignment
# Write a function that returns a string with the characters that appear
# in both input strings, without repetitions. Characters are added in the
# order they appear in the first string.

# Function signature
# def inter(s1: str, s2: str) -> str:

# Examples
# Input
# inter("hello", "world")
# Output
# "lo"
# Input
# inter("banana", "band")
# Output
# "ban"
# Input
# inter("abcabc", "bc")
# Output
# "bc"
# Input
# inter("abc", "xyz")
# Output
# ""
# Input
# inter("", "abc")
# Output
# ""

# Similar to (probably): LeetCode 349. Intersection of Two Arrays
# (set-intersection idea, applied here to characters of two strings while
# preserving first-string order and removing duplicates).
# Reference: question/leetcode/lc349_intersection_of_two_arrays.txt

def inter(s1: str, s2: str) -> str:
    log = ""
    result = ""
    for c in s1:
        if  c not in log and c in s2:
            result += c
        log += c
    return result


if __name__ == "__main__":
    result1 = inter("hello", "world")
    result2 = inter("banana", "band")
    result3 = inter("abcabc", "bc")
    result4 = inter("abc", "xyz")
    result5 = inter("", "abc")

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
