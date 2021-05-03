import math
def pierwiastki_trojmianu(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        return [(-b - math.sqrt(delta))/2*a,(-b + math.sqrt(delta))/2*a]
    elif delta == 0:
        return (b/2*a)
    else:
        return "Trojmian nie posiada pierwiastków w pana ich rozumieniu"

print(pierwiastki_trojmianu(1,6,8))