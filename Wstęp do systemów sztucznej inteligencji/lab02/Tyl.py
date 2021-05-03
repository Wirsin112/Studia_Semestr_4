# Wyszukiawanie od tyłu


def back(look):
    if look in fakty:
        return True
    else:
        for i in range(len(wniosek)):
            if look == wniosek[i]:
                if all(back(x) if len(x) == 1 else not back(x[1]) for x in warunki[i]):
                    return True
    return False


f = [x.strip() for x in open("baza-wiedzy-negacja.txt", 'r').readlines()]
fakty = f[-1].split(',')
if fakty[-1] == '':
    fakty = fakty[0:-1]
wniosek = []
warunki = []
for i in f[:-2]:
    podzielnalinia = i.split('->')
    warunki.append(podzielnalinia[0].split('.')[1].split(','))
    wniosek.append(podzielnalinia[1])
ook = input("Wprowadz warunek:\n")
print(back(ook))
