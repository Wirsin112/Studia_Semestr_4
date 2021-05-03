lista1 = ["Honolulu", "Znaczek", "Pocztowy"]
lista1 = lista1 + ["Wyslij", "Sianko"]
print(lista1)
lista1 = lista1[:1] + ["Dupka pieska"] + lista1[1:]
print(lista1)
lista2 = lista1
print(lista2)
lista2 = lista2 + lista1
print(lista2)
print(len(lista2))
print(lista2[-1])
lista2.remove(lista2[-1])
print(lista2)
del lista2[-1]
print(lista2)
lista3 = lista2[3:6]


