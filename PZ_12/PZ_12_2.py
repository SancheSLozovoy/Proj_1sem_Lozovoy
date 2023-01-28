# Составить генератор (yield), который выводит из строки только цифры.
s = str(input("Введите строку: "))


def str_1(num):
    for i in num:
        if i.isnumeric():
            yield i


g = [i for i in str_1(s)]
print("Цифры из строки:", *g)
