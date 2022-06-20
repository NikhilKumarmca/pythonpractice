num=[]
def even(start,end):
    for i in range(start,end):
        if i%2==0:
            num.append(i)
even(4,30)
print(num)