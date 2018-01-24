def max_val(t):
    Max = -1
    for i in t:
        if type(i)!=int :
            if max_val(i)>Max:
                Max =  max_val(i)
        else:
            if i > Max:
                Max = i
    return Max
print( max_val((5, (1,2), [[1],[9]])) )
