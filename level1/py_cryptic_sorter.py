# py_cryptic_sorter

# Assignment
# Write a function that sorts a list of strings according to multiple criteria:
# 1. Primary sort: by string length (shortest first)
# 2. Secondary sort: ASCII order, but letters are compared case-insensitively
#    (for strings of the same length)
# 3. Tertiary sort: by number of (lowercase) vowels, ascending (for same length
#    and case-insensitively equal strings)
# 4. Equal strings keep their original relative order (stable sort).

# Function signature
# def cryptic_sorter(strings: list[str]) -> list[str]:

# Examples
# Input
# cryptic_sorter(["apple","cat","banana","dog","elephant"])
# Output
# ["cat","dog","apple","banana","elephant"]

# Input
# cryptic_sorter(["aaa","bbb","AAA","BBB"])
# Output
# ["AAA","aaa","BBB","bbb"]

# Input
# cryptic_sorter(["hello","world","hi","test"])
# Output
# ["hi","test","hello","world"]

# Input
# cryptic_sorter([])
# Output
# []

# Input
# cryptic_sorter([""])
# Output
# [""]

# Similar to (probably): No clear direct LeetCode equivalent found; closest inspiration
# is the general "custom multi-key sort" pattern, e.g. LeetCode 179. Largest Number
# (sorting with a custom comparator).

def swap_string(strings: list[str], i: int, j: int) -> None:
    tmp = strings[i]
    strings[i] = strings[j]
    strings[j] = tmp


def check_length(strings1: str, strings2: str) -> bool:
    if len(strings1) < len(strings2):
        return True
    else:
        return False


def check_ascii(string1: str, string2: str) -> bool:
    lenth = min(len(string1), len(string2))
    for i in range(lenth):
        if string1[i].lower() < string2[i].lower():
            return True
    return False


def count_vowels(string: str) -> int:
    vowels = "aeiou"
    count = 0
    for c in string:
        if c in vowels:
            count += 1
    return count


def check_vowels(strings1: str, strings2: str) -> bool:
    count1 = count_vowels(strings1)
    count2 = count_vowels(strings2)
    if count1 < count2:
        return True
    else:
        return False


def primary_sort(strings: list[str]) -> None:
    for i in range(len(strings)):
        for j in range(len(strings)):
            if check_length(strings[i], strings[j]):
                swap_string(strings, i, j)


def secondry_sort(strings: list[str]) -> None:
    for i in range(len(strings)):
        for j in range(len(strings)):
            if check_ascii(strings[i], strings[j]):
                swap_string(strings, i, j)


def tertiary_sort(strings: list[str]) -> None:
    for i in range(len(strings)):
        for j in range(len(strings)):
            if check_vowels(strings[i], strings[j]):
                swap_string(strings, i, j)


def cryptic_sorter(strings: list[str]) -> list[str]:
    tertiary_sort(strings)
    secondry_sort(strings)
    primary_sort(strings)   
    return strings


if __name__ == "__main__":
    strings1 = ["apple","cat","banana","dog","elephant"]
    strings2 = ["aaa","bbb","AAA","BBB"]
    strings3 = ["hello","world","hi","test"]
    strings4 = []
    strings5 = [""]

    return1 = cryptic_sorter(strings1)
    return2 = cryptic_sorter(strings2)
    return3 = cryptic_sorter(strings3)
    return4 = cryptic_sorter(strings4)
    return5 = cryptic_sorter(strings5)

    print(return1)
    print(return2)
    print(return3)
    print(return4)
    print(return5)
