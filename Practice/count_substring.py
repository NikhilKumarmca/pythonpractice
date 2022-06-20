str_x="Emma is good developer and writer . Emma is a writer "
print(str_x)
f = input("Enter word to  find : ")
word = str_x.split()
count=0
for i in word:
    if i == f:
        count +=1
    
print("'{}' is {} time in sentance".format(f,count))
