'''
Given a matrix of integers and coordinates of a rectangular region within the matrix, find the sum of numbers falling inside the rectangle. Our program will be called multiple times with different rectangular regions from the same matrix.

Approach:
Sum = 0
Walk through the matrix, element by element
    if is_in_matrix(x, y):
        sum += matrix[x][y]
    return sum
'''

def matrix_sum(matrix, A, B, C, D):
    result = []
    for x in range(A[0], D[0]+1):
        for y in range(A[1], D[1]+1):
            result.append(matrix[x][y])
    return result

def test_matrix_sum():
    matrix = [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [8, 9, 10, 6]
    ]

    A = (0, 1)
    B = (0, 3)
    C = (1, 1)
    D = (1, 3)
    assert matrix_sum(matrix, A, B, C, D) == [2,3,4,5,6,5]
