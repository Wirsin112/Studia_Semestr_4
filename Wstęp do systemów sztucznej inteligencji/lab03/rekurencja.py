def check_all(x):
    check = []
    for i in range(len(attacker)):
        if deffender[i] == x:
            check.append(attacker[i])
    return check

def check_all_deff(x):
    check = []
    for i in range(len(attacker)):
        if attacker[i] == x:
            check.append(deffender[i])
    return check

def reku(arguments, arguments_in, arguments_out):
    for j in range(len(arguments)):
        args_two = arguments.copy()
        arg_in_two = arguments_in.copy()
        arg_out_two = arguments_out.copy()
        arg_in_two.append(args_two[j])
        args_two.remove(args_two[j])
        bul = True
        while bul:
            bul = False
            i = 0
            while i < len(args_two):
                check = check_all(args_two[i])
                if any(x in arg_in_two for x in check):
                    arg_out_two.append(args_two[i])
                    args_two.remove(args_two[i])
                    bul = True
                else:
                    i += 1
            i = 0
            while i < len(args_two):
                check = check_all_deff(args_two[i])
                if any(x in arg_in_two for x in check):
                    arg_out_two.append(args_two[i])
                    args_two.remove(args_two[i])
                    bul = True
                else:
                    i += 1

            i = 0
            while i < len(args_two):
                check = check_all(args_two[i])
                if all(x in arg_out for x in check):
                    arg_in_two.append(args_two[i])
                    args_two.remove(args_two[i])
                    bul = True
                else:
                    i += 1


        if len(args_two) != 0:
            reku(args_two, arg_in_two, arg_out_two)
        else:
            prefered.append(arg_in_two)

f = [x.strip() for x in open("dung2.txt", 'r').readlines()]
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

i = 0
while i < len(args):
    if args[i] not in deffender:
        arg_in.append(args[i])
        args.remove(args[i])
    else:
        i += 1

bul = True
while bul:
    bul = False
    i = 0
    while i < len(args):
        check = check_all(args[i])
        if any(x in arg_in for x in check):
            arg_out.append(args[i])
            args.remove(args[i])
            bul = True
        else:
            i += 1
    i = 0
    while i < len(args):
        check = check_all(args[i])
        if all(x in arg_out for x in check):
            arg_in.append(args[i])
            args.remove(args[i])
            bul = True
        else:
            i += 1
print("Grounded:", arg_in)
prefered = []
if len(args) != 0:
    reku(args, arg_in, arg_out)

prefered = list(sorted(x) for x in prefered)
prefered = list(set(str(x) for x in prefered))
for i in range(len(prefered)):
    print("Prefered:", prefered[i])
