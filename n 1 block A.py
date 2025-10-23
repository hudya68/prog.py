def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

x = int(input())
n = int(input())

p = power(x, n)
f = factorial(n)

result = p / f
print(result)