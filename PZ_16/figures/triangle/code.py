from math import sqrt
a = 7
b = 2
c = 8


"""Функция для вычисленя периметра треугольника"""


def triangle_perimeter(st_a=a, st_b=b, st_c=c):
    return st_a + st_b + st_c


"""Функция для вычисленя площади треугольника"""


def triangle_area(st_a=a, st_b=b, st_c=c):
    p = (st_a + st_b + st_c) / 2
    return sqrt(p * (p - st_a) * (p - st_b) * (p - st_c))


try:
    print(triangle_perimeter(st_a=float(input("Введите первую сторону треугольника для вычисления периметра ")),
                       st_b=float(input("Введите вторую сторону треугольника для вычисления периметра ")),
                       st_c=float(input("Введите третью сторону треугольника для вычисления периметра "))),
          triangle_area(st_a=float(input("Введите первую сторону треугольника для вычисления площади ")),
                       st_b=float(input("Введите вторую сторону треугольника для вычисления площади ")),
                       st_c=float(input("Введите третью сторону треугольника для вычисления площади "))))
except ValueError:
    print(triangle_perimeter(st_a=a, st_b=b, st_c=c))
    print(triangle_area(st_a=a, st_b=b, st_c=c))
    print("Введены некоректные данные, используются значения по умолчанию")