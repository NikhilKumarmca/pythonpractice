def outer(a,b):
    def add(a,b):
        return a+b
    sum = add(a,b)
    return sum + 5
print(outer(2,4))
