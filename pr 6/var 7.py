n = int(input("Введите количество элементов: "))
a = [int(input("Введите число: ")) for i in range(n)]
print("Массив:", a)

sum_even = 0
prod_odd = 1

for i in range(len(a)):
    if i % 2 == 0:
        sum_even += a[i]
    else:
        prod_odd *= a[i]

print("Сумма элементов с чётными номерами:", sum_even)
print("Произведение элементов с нечётными номерами:", prod_odd)