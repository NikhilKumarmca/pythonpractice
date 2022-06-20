# Write a program to display only those numbers from a list 
list1 = [23,20,155,550,42,26,55]
for i in list1:
    if  i>500:
        break
    elif i>150:
            continue
    elif i%5==0:
        print(i)
print("out of loop")
