str1='James'
print("string is : ",str1)
res = str1[0]
l = len(str1)
mid = int(l/2)
res = res + str1[mid]
res = res + str1[l-1]
print("new string : ",res)
