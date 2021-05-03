def check_list(fun, list):
    return [x for x in list if check(x)]

def check(a):
    return a>5

print(check_list(check,[1,2,3,4,5,6,7]))