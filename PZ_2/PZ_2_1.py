# Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни)
while True:
    try:
        a = int(input("Введите трехзначное число: "))   # ввод переменной
        if a < 100 or a > 999:  # проверка условия
            print("Ошибка, введите трехзначное число")  # вывод ошибки на экран
        else:  # выполняется если условие оказалось ложным
            break  # завершение цикла
    except:
        print("Ошибка, введите трехзначное число!!!")

print("Результат",a // 100, "\nПрограмма завершена!")  # вывод данных, в случае удовлетвоерения всем условиям