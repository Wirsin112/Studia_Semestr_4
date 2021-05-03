f = [x.strip() for x in open("baza2.txt", 'r').readlines()]
fakty = f[-1].split(',')
if fakty[-1] == '':
    fakty = fakty[0:-1]
wniosek = []
warunki = []

for i in f[:-2]:
    podzielnalinia = i.split('->')
    warunki.append(podzielnalinia[0].split('.')[1].split(','))
    wniosek.append(podzielnalinia[1])

bul = True
tab = [0]*len(warunki)
while bul:
    bul = False
    for i in range(len(wniosek)):

        if all(x in fakty if len(x) == 1 else x[-1] not in fakty for x in warunki[i]):
            if wniosek[i] not in fakty:
                tab[i] = 1
                fakty.append(wniosek[i])
                bul = True

        elif wniosek[i] in fakty and tab[i] == 1:
            fakty.remove(wniosek[i])
            bul = True
            tab[i] = 0
print(fakty)