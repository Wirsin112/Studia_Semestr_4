import  sys
wynik = ""
roznica = ord('z') - ord("a")
string = open(sys.argv[1]).read().strip()
for i in range(len(string)):
    if string[i] == ' ':
        wynik += ' '
    elif ord(string[i]) + 2 <= ord('Z'):
        wynik += chr(ord(string[i]) + 2)
    elif ord(string[i]) + 2 <= ord('a'):
        wynik += chr(ord(string[i]) + 1 - roznica)
    elif ord(string[i]) + 2 <= ord('z'):
        wynik += chr(ord(string[i]) + 2)
    else:
        wynik += chr(ord(string[i]) + 1 - roznica)
f = open(sys.argv[2], "w")
f.write(wynik)
