list1 = [23,20,12,25,13,52]
list2 = [22,13,12,19,15,32]
list3 = []
for i in list1:
    if i%2==0:
        list3.append(i)
for j in list2:
    if j%2!=0:
        list3.append(j)
print(list3)