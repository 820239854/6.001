def count7(N):
    if N>0:
        m = N % 10
        N = N // 10
        if m == 7:
            return 1 + count7(N)
        else:
            return 0 + count7(N)
    
    else:
        return 0
print(count7(77777))
