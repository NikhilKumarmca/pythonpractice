s1 = input("Enter first string : ")
s2 = input("Enter sec string : ")

s1len = len(s1)
c=0
for i in s1:
    for j in s2:
        if i == j:
            c += 1

if c == s1len:
    print("True")
else:
    print("False")
