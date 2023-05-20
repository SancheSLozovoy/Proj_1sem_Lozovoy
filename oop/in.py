class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class React(Geom):
    def draw(self):
        print('Рисование прямоугольника')


r = React()
r.set_coords(5, 6, 7, 8)
print(r.__dict__)
print(r.name)
r.draw()

l = Line()
l.set_coords(1, 2, 3, 4)
print(l.__dict__)
print(l.name)
l.draw()
