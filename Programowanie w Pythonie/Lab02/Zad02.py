def fibo(liczba):
    return [a(x) for x in range(liczba)]

def a(n):
    a,b = 0,1
    for i in range(n):
        a, b =b, a+b
    return a
liczba =int(input("Wpisz wielkosc listy\n"))

print(fibo(liczba))