n = int(input("Введите количество элементов: "))
a = [int(input("Введите число: ")) for i in range(n)]
print("Исходный массив:", a)

min_index = a.index(min(a))
max_index = a.index(max(a))

a[min_index], a[max_index] = a[max_index], a[min_index]

print("Массив после обмена минимального и максимального:", a)