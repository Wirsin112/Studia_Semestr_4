def check_all(x):
    for i in range(len(deffender)):
        if deffender[i] == x:
            check.append(attacker[i])

f = [x.strip() for x in open("dane.txt", 'r').readlines()]
args = f[1].split(',')
a = f[-1].split('),(')
a[0] = a[0][1:4]
a[-1] = a[-1][0:3]
attacker = []
deffender = []
for i in range(len(a)):
    attacker.append(a[i].split(',')[0])
    deffender.append(a[i].split(',')[1])
# for i in range(len(a)):
#     print(attacker[i], deffender[i])
arg_in = []
arg_out = []
bul = True
for i in range(len(args)-1):
    if args[i] not in deffender:
        arg_in.append(args[i])
        args.remove(args[i])

while bul:
    bul = False
    for i in range(len(args)-1):
        check = []
        check_all(args[i])
        if any(x in arg_in for x in check):
            arg_out.append(args[i])
            args.remove(args[i])
            bul = True
    for i in range(len(args)-1):
        check = []
        check_all(args[i])
        if all(x in arg_out for x in check):
            arg_in.append(args[i])
            args.remove(args[i])
            bul = True


print("Grounded:", arg_in)
for j in range(len(args)):
    args_two = args.copy()
    arg_in_two = arg_in.copy()
    arg_out_two = arg_out.copy()
    arg_in_two.append(args_two[j])
    args_two.remove(args_two[j])
    bul = True
    while bul:
        bul = False
        for i in range(len(args_two) - 1):
            check = []
            check_all(args_two[i])
            if any(x in arg_in_two for x in check):
                arg_out_two.append(args_two[i])
                args_two.remove(args_two[i])
                bul = True
        for i in range(len(args_two) - 1):
            check = []
            check_all(args_two[i])
            if all(x in arg_out for x in check):
                arg_in_two.append(args_two[i])
                args_two.remove(args_two[i])
                bul = True
    print("Prefered:", arg_in_two)
print('finished')