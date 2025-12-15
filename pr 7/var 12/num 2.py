import math
def median(a, b, c):
    return math.sqrt((2*b**2 + 2*c**2 - a**2) / 4)
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)
ma2 = median(ma, mb, mc)
mb2 = median(mb, ma, mc)
mc2 = median(mc, ma, mb)
print("Медианы нового треугольника:", ma2, mb2, mc2)
