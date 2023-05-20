# Создайте класс "Прямоугольник" с атрибутами длины и ширины.
# Добавьте методы для вычисления площади и периметра.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def square(self):
        return f'Площадь: {self.width * self.height}'


    def perimeter(self):
        return f'Периметр: {(self.width * 2) + (self.height * 2)}'


rectangle = Rectangle(5, 3)


print(rectangle.square())
print(rectangle.perimeter())

