n = int(input("Введите количество элементов: "))
x = [int(input("Введите число: ")) for i in range(n)]
print("Массив:", x)
min_value = min(x)
min_index = x.index(min_value)
print("Минимальный элемент:", min_value)
print("Индекс минимального элемента:", min_index)