# Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
# целые степени числа A от 1 до N.
try:  # обработка исключений
    a = float(input("Введите вещественное число: "))  # задаю две переменные
    n = int(input("Введите целое число: "))
    n1 = 1
    if n < 0:  # создание условий
        print("Ошибка, n>0")
    else:
        while n1 != n:  # задача цикла
            print("Результат:", a ** n1)  # вывод результата
            n1 += 1
except ValueError:
    print("Введены некорректные данные")
