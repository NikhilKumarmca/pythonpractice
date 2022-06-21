s1 = "Ault"
s2 = "Kelly"

mid = len(s1)//2
s3 = s1[:mid:]
s3 = s3 + s2
s3 = s3 + s1[mid:]
print(s3)