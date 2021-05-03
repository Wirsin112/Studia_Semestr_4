def a(napis):
    return [(x,len(x)) for x in napis.split()]
string = "Ala ma kota a Kotyra nie ma kolegow"
print(a(string))