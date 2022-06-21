from symtable import Symbol


str1 = "P@#yn26at^&i5ve"
letter,digit,symbol = 0,0,0
for i in str1:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    else:
        symbol += 1
print("letter is : {}\nDigit is : {}\nSymbol is : {}".format(letter,digit,symbol))
