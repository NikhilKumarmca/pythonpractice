from functools import reduce
nums = [4,3,2,5,7,2,1,6,9]
evens = list(filter(lambda n:n%2==0,nums))
odds = list(filter(lambda n:n%2==1,nums))
print(evens)
print(odds)

doubles = list(map(lambda n:n*2,evens))
triple = list(map(lambda n:n*3,odds))

print(doubles)
print(triple)

sumdouble = reduce(lambda n,m:n+m,doubles)
sumtriple = reduce(lambda n,m:n+m,triple)

print(sumdouble)
print(sumtriple)