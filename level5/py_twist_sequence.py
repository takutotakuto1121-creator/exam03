# py_twist_sequence

# Assignment
# Write a function that rotates an array to the right by k positions.
# Rotating right by k means the last k elements move to the front.

# Function signature
# def twist_sequence(arr: list[int], k: int) -> list[int]:

# Examples
# Input
# twist_sequence([1,2,3,4,5], 2)
# Output
# [4,5,1,2,3]
# Input
# twist_sequence([1,2,3], 1)
# Output
# [3,1,2]
# Input
# twist_sequence([1,2,3,4], 0)
# Output
# [1,2,3,4]
# Input
# twist_sequence([1,2,3], 5)
# Output
# [2,3,1]
# Input
# twist_sequence([], 3)
# Output
# []

# Similar to (probably): LeetCode 189. Rotate Array (identical problem).
# Reference: question/leetcode/lc189_rotate_array.txt

def swap(arr: list[int], i: int, j: int) -> None:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                swap(arr, i, j)


def rotate(arr: list[int], k: int) -> None:
    length = len(arr)
    result = [0] * length
    for i in range(length):
            result[(i + k) % length] = arr[i]
    return result


def twist_sequence(arr: list[int], k: int) -> list[int]:
    bubble_sort(arr)
    result = rotate(arr, k)
    return result


if __name__ == "__main__":
    print(twist_sequence([1,2,3,4,5], 2))
    print(twist_sequence([1,2,3], 1))
    print(twist_sequence([1,2,3,4], 0))
    print(twist_sequence([1,2,3], 5))
    print(twist_sequence([], 3))
