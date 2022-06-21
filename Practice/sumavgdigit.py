str1 = "PYnative29@#8496"
sum =0
c = 0
for i in str1:
    if i.isdigit():
        sum += int(i)
        c += 1
print("sum is : ",sum)
print("avarage is : ",sum/c)