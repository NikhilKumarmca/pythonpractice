s1 = "Abc"
s2 = "Xyz"

s1len = len(s1)
s2len = len(s2)
length = s1len if s1len >s2len else s2len
res = ""
s2 = s2[::-1]
for i in range(length):
    if i < s1len :
        res = res + s1[i]
    if i < s2len:
        res = res + s2[i]
print(res)