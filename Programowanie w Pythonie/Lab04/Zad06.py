import  math
def print_width(x):
    f = open("zad06.txt").read().strip()
    l = math.ceil(len(f)/int(x))
    for i in range(l):
        abc = ""
        abc = f[i*int(x):int(x)*i+int(x)]
        print(abc.center(int(x)))
x = input("Width = ")
print_width(x)