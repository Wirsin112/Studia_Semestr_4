# easda
f = [x.strip() for x in open("Wnioski.txt", 'r').readlines()]
fakty = f[-1].split(',')
wniosek = []
warunki = []
a = 0
for i in f[:-2]:
    podzielnalinia = i.split()
    warunki.append(podzielnalinia[1].split(','))
    wniosek.append(podzielnalinia[3])
bul = True
while bul:
    bul = False
    for i in range(len(wniosek)):
        if all(x in fakty for x in warunki[i]):
            if wniosek[i] not in fakty:
                fakty.append(wniosek[i])
                bul = True

print(fakty)