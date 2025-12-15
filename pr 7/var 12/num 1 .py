def sum_of_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum
N = int(input("Введите число N: "))
friendly_pairs = []
for i in range(2, N+1):
    for j in range(i+1, N+1):
        if sum_of_divisors(i) == j and sum_of_divisors(j) == i:
            friendly_pairs.append((i, j))
print("Пары дружественных чисел:", friendly_pairs)
