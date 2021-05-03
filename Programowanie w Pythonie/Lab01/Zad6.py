n = input("Ile chcesz liczb wrpowadzic\n")
a,b = 0, 1
for i in range(int(n)):
    print(b, end=' ')
    tmp = b
    b = a+b
    a = tmp


