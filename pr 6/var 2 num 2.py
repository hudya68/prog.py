n = int(input("Введите количество элементов: "))
a = [int(input("Введите число: ")) for i in range(n)]
print("Исходный массив:", a)

positive = []
others = []

for i in a:
    if i > 0:
        positive.append(i)
    else:
        others.append(i)

print("Положительные элементы:", positive)
print("Остальные элементы:", others)