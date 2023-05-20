# 14.Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
# унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
# вычисления площади и периметра
class Form:
    def __init__(self, color, type):
        self.color = color
        self.type = type


class Circle(Form):
    def __init__(self, color, type, radius):
        self.radius = radius

    def area(self):
        return f"Площадь круга: {3.14 * (self.radius**2)}"

    def per(self):
        return f"Периметр круга: {2 * 3.14 * self.radius}"


cir = Circle("Синий", "круг", 5)
print(cir.area())
print(cir.per())