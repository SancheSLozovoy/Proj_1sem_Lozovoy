from math import pi

default_radius = 5

"""Функция для вычисления длины окружности"""


def circle_perimeter(r=default_radius):
    return pi * r * 2


"""Функция для вычисления площали круга"""


def circle_area(r=default_radius):
    return pi * r ** 2
