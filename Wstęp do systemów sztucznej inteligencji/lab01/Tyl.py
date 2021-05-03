# Wyszukiawanie od tyłu


def back(look):
    if look in fakty:
        return True
    else:
        for i in range(len(wniosek)):
            if look == wniosek[i]:
                if all(back(x) for x in warunki[i]):
                    return True
    return False


f = [x.strip() for x in open("Baza.txt", 'r').readlines()]
fakty = f[-1].split(',')
wniosek = []
warunki = []
a = 0
for i in f[:-2]:
    podzielnalinia = i.split()
    warunki.append(podzielnalinia[1].split(','))
    wniosek.append(podzielnalinia[3])
ook = input("Wprowadz warunek:\n")
print(back(ook))
