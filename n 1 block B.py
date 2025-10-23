def f():
    x = int(input())
    if x == 0:
        return x
    y = f()
    if x > y:
        return x
    else:
        return y

print(f())