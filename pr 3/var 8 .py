x = int(input("Введите x: "))
y = int(input("Введите y: "))
if x < y:
    B = x * y
elif x > y:
    B = y + x
else:
    B = x + y
print("B =", B)
