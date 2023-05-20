# Николаю требуется проверить, возможно ли из представленных
# отрезков условной длины сформировать треугольник. Для этого
# он решил создать класс Triangle Checker, принимающий только
# положительные числа. С помощью метода is_triangle()
# возвращаются следующие значения (в зависимости от ситуаций)
# -Ура, можно построить треугольник!
# -С отрицательными числами ничего не выйдет!
# -Нужно вводить только числа!
# -Жаль, но из этого треугольник не сделать


class TriangleChecker:
    def dlin_triangle(self, a=2, b=2, c=4):
        print('Вызов метода set_coords для' + str(self))
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if type(a) != int and type(b) != int and type(c) != int:
            return '-Нужно вводить только чиса'
        else:
            if a >= 0 and b >= 0 and c >= 0:
                if a + b > c and c + b > a and a + c > b:
                    return '-Ура, можно построить треугольник!'
                else:
                    return '-Жаль, но из этого треугольник не выйдет!'
            else:
                return '-С отрицательными числами ничего не выйдет!'


q = TriangleChecker()
q.dlin_triangle(a = int(input('Введите первую сторону: ')),
                b = int(input('Введите вторую сторону: ')),
                c = int(input('Введите третью сторону: ')))
print(q.is_triangle())