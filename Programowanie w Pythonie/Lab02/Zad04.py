import math
def key(e):
    return math.dist(e,point)
def check_distance(array,point):
    array.sort(key=key)
    return [(math.dist(x,point),x) for x in array]
point = (1,1)
array = [(1, 2), (1, 3)]
print(check_distance(array, point))
