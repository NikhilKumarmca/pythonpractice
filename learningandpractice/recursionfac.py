def recfac(n):
    if(n==0):
        return 1
    return n * recfac(n-1)
print(recfac(4))