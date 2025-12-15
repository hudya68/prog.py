m = int(input("Введите длину массива: "))
A = []
for i in range(m):
    A.append(int(input(f"Введите элемент {i+1}: ")))
A[0], A[-1] = A[-1], A[0]
print("Массив после замены элементов:", A)
