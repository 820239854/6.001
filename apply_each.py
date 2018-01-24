def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])



def abs(x):
    if x>0:
        return x
    else:
        return  -x

def addOne(x):
    return x+1

def square(x):
    return x*x
applyToEach(testList,square)
print( testList )
    
