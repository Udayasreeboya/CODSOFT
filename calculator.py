a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
select=print("Please select an operator \n" \
        "1.Addition\n" \
        "2.subtraction\n" \
        "3.Multiplication\n"
        "4.Dision\n")
c=int(input("Select an operation:"))

if c == 1:
    print("result:",a+b)
elif c == 2:
    print("result:",a-b)
elif c == 3:
    print("result:",a*b)
elif c == 4:
    print("result:",a/b)
else:
    print("Enter an valid operator")
