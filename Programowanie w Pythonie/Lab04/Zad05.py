import sys
a = [x.strip() for x in open(sys.argv[1]).readlines()]
b = [x.strip() for x in open(sys.argv[2]).readlines()]
res = []
res.append("File 1")
for x in a:
    if x not in b:
        res.append(x)
res.append("File 2")
for x in b:
    if x not in a:
        res.append(x)

with open(sys.argv[3], 'w') as f:
    for i in res:
        f.write(i+"\n")