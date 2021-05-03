jump = input("Wrowadz przeskok\n")
for i in range(ord('a'),ord('z'),int(jump)):
    mala = chr(i)
    duza = mala.upper()
    print(mala+" "+duza)