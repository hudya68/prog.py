def is_divisible_by_digits(num):
    num_str = str(num)  
    for digit in num_str:
        digit = int(digit)  
        if digit == 0 or num % digit != 0:  
            return False
    return True
n = int(input("Введите число n: "))
result = []
for i in range(1, n+1):
    if is_divisible_by_digits(i):
        result.append(i)

print("Числа, которые делятся на каждую свою цифру:", result)
