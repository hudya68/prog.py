n = int(input("Введите n: "))

fact = 1      
summa = 0     

for i in range(1, n + 1):
    fact *= i        
    summa += fact    

print("Сумма факториалов:", summa)
