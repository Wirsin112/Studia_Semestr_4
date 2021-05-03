def make_dict(file):
    dict = {}
    f = [x.strip() for x in open(file).readlines()]
    for x in f:
        dict[x.split(":")[0]] = x.split(":")[1].strip()
    return dict


print(make_dict("zad02.txt"))
