from math import pi

default_radius = 5


def circle_perimeter(r=default_radius):
    return pi * r * 2


def circle_area(r=default_radius):
    return pi * r ** 2


try:
    print(circle_perimeter(r=float(input("Введите радиус окружности: "))))
except ValueError:
    print(circle_perimeter(r=default_radius))

try:
    print(circle_area(r=float(input("Введите радиус окружноси: "))))
except ValueError:
    print(circle_area(r=default_radius))
