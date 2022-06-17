a=4
b=2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter any number"))
    print(k)
except ZeroDivisionError as e:
    print("oops.. this error occur cause of zero in denominator ")
except ValueError as e:
    print("oops.. this error occur cause of enter invalid input")
except Exception as e:
    print("something went wrong")

finally:
    print("Resource Close")