class Punkt2D:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, Punkt):
        return ((self.x - Punkt.x) ** 2 + (self.y - Punkt.y) ** 2) ** 0.5


class Punkt3D(Punkt2D):
    z = None

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, Punkt):
        return ((self.x - Punkt.x) ** 2 + (self.y - Punkt.y) ** 2 + (self.z - Punkt.z)) ** 0.5
