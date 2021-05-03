ilosc = input("Ile liczb chcesz \n")
liczby = []
for i in range(int(ilosc)):
    liczby.append(int(input("Wprowadz liczbe nr "+str(i)+"\n")))
typ = input("Wprowadz 0 jezeli sortownie rosnace.Wprowdz cokolwiek innego jak malejace\n")
dol = input("Podaj dolny zakres \n")
gora = input("Podaj dolny zakres \n")
if typ == "0":
    liczby.sort()
    for i in liczby:
        if int(i) > int(dol) and int(i) < int(gora):
            print(i)
else:
    liczby.sort(reverse=True)
    for i in liczby:
        if int(i) > int(dol) and int(i) < int(gora):
            print(i)