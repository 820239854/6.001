def satisfiesF(L):
    count = 0
    L_copy = L[:]
    for i in L_copy:
        if not f(i):
            L.remove(i)
        else:
            count+=1
    return count

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print (satisfiesF(L))
print (L)
