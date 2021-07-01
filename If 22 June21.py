num = int(input("Enter your number"))
if num >= 0:
    if num == 0:
        print("It's a zero number")
    else:
        print("{0} is a positive number" .format(num))
else:
    print("{0} is a negative number" .format(num))