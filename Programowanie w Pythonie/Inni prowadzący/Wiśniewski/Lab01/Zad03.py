lista1 = ['1']*100
lista2 = ['a']*100
lista3 = lista1+lista2
lista4 = lista3[23:132]
print(len(lista4))
print(lista4.count('1'))
print(lista4.count('a'))
print(lista4.index('a'))
