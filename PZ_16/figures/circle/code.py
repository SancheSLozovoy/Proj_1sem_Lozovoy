from math import pi

default_radius = 5

"""Функция для вычисления длины окружности"""


def circle_perimeter(r=default_radius):
    return pi * r * 2


"""Функция для вычисления площали круга"""


def circle_area(r=default_radius):
    return pi * r ** 2


try:
    print(circle_perimeter(r=float(input("Введите радиус окружности для вычисления длины окружности: "))),
          circle_area(r=float(input("Введите радиус окружноси для вычисления площали круга: "))))
except ValueError:
    print(circle_perimeter(r=default_radius))
    print(circle_area(r=default_radius))
