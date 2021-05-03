#Generalnie to działa ale nie wiem czy tak jak Pan chciał ale działa
#Ps listy są kozak a reszta nie
def set_pos_cons():
    a = []
    for i in range(len(con1)):
        if len(con2[i]) == 0:
            a.append(con1[i])
    return list(set(a))

def return_posibility2(result, cons):
    check = [con3[x] for x in range(len(con3)) if con1[x] == result and set(con2[x]) == set(cons)]
    if len(check) != 0:
        return check[0]
    a = [con2[x] for x in range(len(con2)) if con1[x] == result if con2[x] != [] and x < stop]
    a = [a[x] for x in range(len(a)) if all('~' + y not in a[x] for y in cons)]
    posibility = 0
    for d in a:
        p1 = float([con3[x] for x in range(len(con3)) if con1[x] == result and all(y in con2[x] for y in d)][0])
        for i in d:
            if i[0] != "~":
                if i not in cons:
                    if len([con3[x] for x in range(len(con3)) if con1[x] == i and set(con2[x]) == set(cons)]) != 0:
                        p1 *= float([con3[x] for x in range(len(con3)) if con1[x] == i and set(con2[x]) == set(cons)][0])
                    else:
                        if i not in true_cons:
                            con1.append(i)
                            con2.append(cons)
                            con3.append(return_posibility2(i, cons))
                            p1 *= float(
                                [con3[x] for x in range(len(con3)) if con1[x] == i and set(con2[x]) == set(cons)][0])
                        else:
                            p1 *= float([con3[x] for x in range(len(con3)) if con1[x] == i and con2[x] == []][0])
            else:
                if len([con3[x] for x in range(len(con3)) if con1[x] == i[1:] and set(con2[x]) == set(cons)]) != 0:
                    p1 *= (1 - float([con3[x] for x in range(len(con3)) if con1[x] == i[1:] and set(con2[x]) == set(cons)][0]))
                else:
                    if i[1:] not in true_cons:
                        con1.append(i[1:])
                        con2.append(cons)
                        con3.append(return_posibility2(i[1:], cons))
                        p1 *= (1 - float([con3[x] for x in range(len(con3)) if con1[x] == i[1:] and set(con2[x]) == set(cons)][0]))
                    else:
                        p1 *= (1 - float([con3[x] for x in range(len(con3)) if con1[x] == i[1:] and con2[x] == []][0]))
        posibility += p1
    return posibility

if __name__ == "__main__":
    f = [x.strip() for x in open("bayes.txt").readlines()]
    nodes = f[1].split(',')

    con3 = [f[x].split('=')[1].strip() for x in range(5, len(f))]
    a = [f[x].split('=')[0].strip() for x in range(5, len(f))]
    con1 = [a[x][2:-1].split('|')[0] for x in range(len(a))]
    con2 = [a[x][2:-1].split('|')[1].split(',') if '|' in a[x][2:-1] else [] for x in range(len(a))]
    stop = len(con1)

    true_cons = set_pos_cons()

    a = ''
    print("Wprowadz - exit jeśli chcesz skończyć")
    print("Wprowadz - info jeśli chcesz dostać listę wyników i wniosków")
    while a != 'exit':
        can = True
        a = input("Wprowadz warunek\n")
        if a == 'info':
            print("Dostepne wyniki:", nodes)
            print("Dostepne warunki:", true_cons)
        elif a != 'exit':
            if "|" in a:
                a_cons = a[2:-1].split('|')[1].split(",")
                a_res = a[2:-1].split('|')[0]
                if a_res not in nodes:
                    can = False
                    print("Nie ma takiego wyniku jaki chcesz sprawdzic")
                elif a_res in true_cons:
                    print("Ten wynik nie może przyjąć warunków")
                    can = False
                if any(x not in true_cons for x in a_cons):
                    print("Warunki jakie nie podałeś nie zawierają się w warunakch jakie możesz użyć")
                    print("Warunki jakie możesz użyć", true_cons)
                    can = False
            else:
                a_res = a[2:-1]
                a_cons = []
                if a_res not in nodes:
                    can = False
                    print("Nie ma takiego wyniku jaki chcesz sprawdzic")
            if can:
                print(return_posibility2(a_res, a_cons))