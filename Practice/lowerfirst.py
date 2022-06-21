str1 = "PyNaTive"
low = []
up = []
for i in str1:
    if i.islower():
        low.append(i)
    else:
        up.append(i)
str2 = ''.join(low+up)
print(str2)