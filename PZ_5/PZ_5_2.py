# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить левый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def ShiftLeft3(a, b, c):
    x = a
    y = b
    z = c
    print(a, b, c)
    c1 = x
    b1 = z
    a1 = y
    print(a1, b1, c1)
    a2 = b1
    b2 = c1
    c2 = a1
    print(a2, b2, c2)


ShiftLeft3(a=float(input("Введите число: ")), b=float(input("Введите число: ")), c=float(input("Введите чило: ")))
