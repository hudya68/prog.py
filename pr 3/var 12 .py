a = int(input("Введите a: "))
b = int(input("Введите b: "))
if a < b:
    R = a - b
elif a > b:
    R = b - a
else:
    R = -b
print("R =", R)
