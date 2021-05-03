import math
class Liczba():
    lista = []

    def __init__(self, string):
        self.lista = []
        for i in range(len(string)):
            self.lista.append(int(string[i]))
    def multi(self,number):
        a = ""
        for i in range(len(self.lista)):
            a = a + str(self.lista[i])
        a = int(a)
        a = a*number
        self.__init__(str(a))
    def silnia(self):
        a = ""
        for i in range(len(self.lista)):
            a = a + str(self.lista[i])
        a = int(a)
        return math.factorial(a)
a = Liczba("5")
print(a.lista)
print(a.silnia())
