from itertools import count


num = int(input("Enter any number : "))
c=0
while num>0:
    num = num//10
    c = c+1
print("number of digit : ",c)
