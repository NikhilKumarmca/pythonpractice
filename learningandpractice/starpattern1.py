
k=1243
rev = 0
while k!=0:
    r = k % 10
    rev = rev * 10 + r
    k = k // 10
print(rev)


