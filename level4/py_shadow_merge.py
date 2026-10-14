# py_shadow_merge

# Assignment
# Write a function that merges two already-sorted lists into one sorted
# list.

# Function signature
# def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

# Examples
# Input
# shadow_merge([1,3,5], [2,4,6])
# Output
# [1,2,3,4,5,6]
# Input
# shadow_merge([1,2,3], [4,5,6])
# Output
# [1,2,3,4,5,6]
# Input
# shadow_merge([1], [2,3,4])
# Output
# [1,2,3,4]
# Input
# shadow_merge([], [1,2,3])
# Output
# [1,2,3]
# Input
# shadow_merge([1,1,2], [1,3,3])
# Output
# [1,1,1,2,3,3]

# Similar to (probably): LeetCode 21. Merge Two Sorted Lists (same merge
# algorithm; LeetCode uses a linked list, here it is plain Python lists).
# Reference: question/leetcode/lc021_merge_two_sorted_lists.txt


def swap(merge: list[int], i: int, j: int) -> None:
    tmp = merge[i]
    merge[i] = merge[j]
    merge[j] = tmp


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merge = []
    for part in list1:
        merge.append(part)
    for part in list2:
        merge.append(part)

    for i in range(len(merge)):
        for j in range(len(merge)):
            if merge[i] < merge[j]:
                swap(merge, i, j)

    return merge


if __name__ == "__main__":
    print(shadow_merge([1,3,5], [2,4,6]))
    print(shadow_merge([1,2,3], [4,5,6]))
    print(shadow_merge([1], [2,3,4]))
    print(shadow_merge([], [1,2,3]))
    print(shadow_merge([1,1,2], [1,3,3]))
