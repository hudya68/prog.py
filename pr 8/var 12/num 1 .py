def find_matching(matrix):
    for k in range(len(matrix)):
        if matrix[k] == [matrix[i][k] for i in range(len(matrix))]:
            print(f"Строка {k+1} совпадает с столбцом {k+1}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

find_matching(matrix)
