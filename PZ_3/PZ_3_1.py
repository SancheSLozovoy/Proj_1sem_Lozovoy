#Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его. Вывести получкенное число
try:  # обраюотка исключений
    a = int(input("Введите целое число: "))  # создание переменной
    if a >= 1:  # условие
        print("Результат:", a + 1)
    else:
        print(a)
except:
    print("Ошибка, введите целое число!")