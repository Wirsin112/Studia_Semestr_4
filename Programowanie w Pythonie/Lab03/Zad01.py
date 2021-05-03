class Liczby_zespolone:
    czesc_rzeczywista = None
    czesc_urojona = None

    def __str__(self):
        if self.czesc_urojona < 0:
            return str(self.czesc_rzeczywista) + str(self.czesc_urojona) + "i"
        else:
            return str(self.czesc_rzeczywista) + "+" + str(self.czesc_urojona) + "i"

    def __add__(self, other):
        a = Liczby_zespolone()
        a.set_rzeczyywista(self.czesc_rzeczywista + other.czesc_rzeczywista)
        a.set_urojona(self.czesc_urojona + other.czesc_urojona)
        return a

    def __sub__(self, other):
        a = Liczby_zespolone()
        a.set_rzeczyywista(self.czesc_rzeczywista - other.czesc_rzeczywista)
        a.set_urojona(self.czesc_urojona - other.czesc_urojona)
        return a

    def __truediv__(self, other):
        a = Liczby_zespolone()
        dzielnik = other.czesc_rzeczywista ** 2 + other.czesc_urojona ** 2

        a.set_rzeczyywista(
            (self.czesc_rzeczywista * other.czesc_rzeczywista - self.czesc_urojona * other.czesc_urojona) / dzielnik)
        a.set_urojona(
            (self.czesc_rzeczywista * other.czesc_urojona + self.czesc_urojona * other.czesc_rzeczywista) / dzielnik)
        return a

    def __mul__(self, other):
        a = Liczby_zespolone()
        a.set_rzeczyywista(self.czesc_rzeczywista * other.czesc_rzeczywista - self.czesc_urojona * other.czesc_urojona)
        a.set_urojona(self.czesc_urojona * other.czesc_rzeczywista + self.czesc_rzeczywista * other.czesc_urojona)
        return a

    def __eq__(self, other):
        if self.modul() == other.modul():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.modul() < other.modul():
            return True
        else:
            return False

    def __le__(self, other):
        if self.modul() <= other.modul():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.modul() != other.modul():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.modul() > other.modul():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.modul() >= other.modul():
            return True
        else:
            return False

    def set_rzeczyywista(self, czesc_rzeczywista):
        self.czesc_rzeczywista = czesc_rzeczywista

    def set_urojona(self, czesc_urojona):
        self.czesc_urojona = czesc_urojona

    def modul(self):
        return (self.czesc_rzeczywista ** 2 + self.czesc_urojona ** 2) ** 0.5


a = Liczby_zespolone()
b = Liczby_zespolone()
a.set_rzeczyywista(1)
a.set_urojona(8)
b.set_rzeczyywista(8)
b.set_urojona(1)
print(a >= b)
