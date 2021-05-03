import sys


def make_dict(file):
    dicta = {}
    f = open(file).read().strip().split(' ')
    for x in f:
        if dicta.get(x) != None:
            dicta[x] += 1
        else:
            dicta[x] = 1
    return dicta


make_dict(sys.argv[1])
