s = input("Введите строку: ")

n = len(s)                
half = n // 2             
result = ""               

for i in range(n):
    if i < half and s[i] == 'п':
        result += '*'    
    else:
        result += s[i]    

print("Преобразованная строка:", result)