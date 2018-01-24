import math 
def polysum(n, s):
    return round( (0.25*n*s*s/math.tan(pi/n)) + math.pow(n*s, 2), 4)
