def a(napis):
    return [(x,len(x)) for x in napis.split()]
string = "Ala ma Kota"
print(a(string))