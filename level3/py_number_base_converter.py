# py_number_base_converter

# Assignment
# Write a function that converts a number (given as a string) from one
# base to another. Support bases from 2 to 36 inclusive. Use digits 0-9
# and letters A-Z for values 10-35. Return "ERROR" for invalid inputs
# (invalid base, empty string, or a digit that does not belong to
# from_base).

# Function signature
# def number_base_converter(number: str, from_base: int, to_base: int) -> str:

# Examples
# Input
# number_base_converter("1010", 2, 10)
# Output
# "10"
# Input
# number_base_converter("FF", 16, 10)
# Output
# "255"
# Input
# number_base_converter("255", 10, 16)
# Output
# "FF"
# Input
# number_base_converter("123", 10, 2)
# Output
# "1111011"
# Input
# number_base_converter("Z", 36, 10)
# Output
# "35"
# Input
# number_base_converter("35", 10, 36)
# Output
# "Z"
# Input
# number_base_converter("123", 1, 10)
# Output
# "ERROR"
# Input
# number_base_converter("G", 16, 10)
# Output
# "ERROR"

# Similar to (probably): No exact match; loosely related to LeetCode 504.
# Base 7 (converting a decimal number to a single fixed base), generalized
# here to arbitrary bases 2-36 in both directions.

def get_base(base: int) -> str:
    base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return base_str[:base]


def atoi_base(number: str, from_base: int) -> int:
    result = 0
    base = get_base(from_base)
    # print(base)
    for c in number:
        pos = base.find(c)
        if pos == -1:   # findのエラー
            return (-1)
        result = result * from_base + pos
    # print(result)
    return result


def itoa_base(number: int, to_base: int) -> str:
    if number == 0:
        return "0"
    base = get_base(to_base)
    result = ""
    while number > 0:
        result += base[number % to_base]
        number //= to_base
    return result


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    if not number:
        return "ERROR"

    number_decimal = atoi_base(number, from_base)
    if number_decimal == -1:
        return "ERROR"

    result = itoa_base(number_decimal, to_base)

    reversed_result = ""
    for i in range(len(result) -1 , -1, -1):
        reversed_result += result[i]

    return reversed_result


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))
