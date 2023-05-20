class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_coord(self, x, y):
        self._x = x
        self._x = y

pt = Point(1, 2)
print(pt._x, pt._y)