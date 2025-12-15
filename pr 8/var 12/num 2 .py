def subtract_last_row(matrix):
    last_row = matrix[-1]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            matrix[i][j] -= last_row[j]
    print(matrix)
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
subtract_last_row(matrix)
