a = 15

"""Функция для вычисленя периметра квадрата"""


def square_perimeter(st=a):
    return st * 4


"""Функция для вычисления площади квадрата"""


def square_area(st=a):
    return st ** 2


try:
    print(square_perimeter(st=float(input("Введите сторону квадарата для вычисления его периметра: "))),
          square_area(st=float(input("Введите сторону квадрата для вычисления его площади: "))))
except ValueError:
    print(square_perimeter(st=a))
    print(square_area(st=a))
