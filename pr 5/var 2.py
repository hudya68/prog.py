s = input("Введите строку: ")

count = s.count(':')         
s = s.replace(':', '%')      
print("Изменённая строка:", s)
print("Количество замен:", count)