def topten():
    n=1
    while n<= 20:
        sq = n*2
        yield sq
        n +=1
nums = topten()

for i in nums:
    print(i)