rag = int(input("Enter your range : "))
j=0
for i in range(rag):

    print("Current Number {0} previous number {1} sum: {2}".format(i,j,i+j))
    j=i