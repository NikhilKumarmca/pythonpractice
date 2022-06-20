start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))
for i in range(start,end+1):
    if i > 1:
        for num in range(2,i):
            if (i%num)==0:
                break
        else:
            print(i)
                