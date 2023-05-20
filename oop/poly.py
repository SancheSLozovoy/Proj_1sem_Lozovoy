class Geom:
    def get_pr(self):
        raise NotImplementedError("")


class Rectange:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.h + self.w)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectange(1, 2)
r2 = Rectange(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(2, 4, 6)
# print(r1.get_rech_pr(), r2.get_rech_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())

geom = [Rectange(1, 2), Rectange(3,4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 2, 3)]

for g in geom:
    print(g.get_pr())