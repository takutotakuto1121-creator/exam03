# py_mirror_matrix

# Assignment
# Given a 2D matrix (list of lists), return a new matrix where each row
# is reversed.

# Function signature
# def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:

# Examples
# Input
# mirror_matrix([[1,2,3],[4,5,6]])
# Output
# [[3,2,1],[6,5,4]]
# Input
# mirror_matrix([[1,2],[3,4],[5,6]])
# Output
# [[2,1],[4,3],[6,5]]
# Input
# mirror_matrix([[7]])
# Output
# [[7]]
# Input
# mirror_matrix([[1,2,3,4]])
# Output
# [[4,3,2,1]]
# Input
# mirror_matrix([[-1,-2],[-3,-4]])
# Output
# [[-2,-1],[-4,-3]]

# Similar to (probably): No single well-known LeetCode problem matches this
# exactly; row-reversal is a building block used inside LeetCode 48. Rotate
# Image (rotating a matrix in place).

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for part in matrix:
        reverse_part = []
        for i in range(len(part) - 1, -1, -1):
            reverse_part.append(part[i])
        result.append(reverse_part)
    return result


if __name__ == "__main__":
    result1 = mirror_matrix([[1,2,3],[4,5,6]])
    result2 = mirror_matrix([[1,2],[3,4],[5,6]])
    result3 = mirror_matrix([[7]])
    result4 = mirror_matrix([[1,2,3,4]])
    result5 = mirror_matrix([[-1,-2],[-3,-4]])

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    

