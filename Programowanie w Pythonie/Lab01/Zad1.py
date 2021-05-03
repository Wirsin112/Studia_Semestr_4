name = input("Podaj imie i nazwisko\n")
age = input("Podaj wiek\n")
if int(age) >= 18:
    print("Czesc "+name+" jestes pelnoletni")
else:
    print("Czesc " + name + " jestes niepelnoletni")