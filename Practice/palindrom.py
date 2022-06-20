num = int(input("enter any number : "))
temp = num
num1=0
while(num>0):
    rem  = num%10
    num1 = num1*10+rem
    num = num // 10
if num1 == temp:
    print("yes, given number is palindrom ")
    
else:
    print("No, given number is not palindrom")