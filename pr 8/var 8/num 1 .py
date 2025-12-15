def divide_kth_row(matrix, k):
    diagonal_element = matrix[k][k]  
    for i in range(len(matrix[k])):
        matrix[k][i] = matrix[k][i] / diagonal_element  
    print(matrix) 
matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
k = 1  
divide_kth_row(matrix, k)