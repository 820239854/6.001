def genPrimes():
    n = 2
    Primes = []
    found = True
    while True:
        for p in Primes:
            if n%p == 0:
                found = False
        if found == True:
            Primes.append(n)
##            print(Primes)
            yield n
        n += 1
        found = True
p = genPrimes()
            
