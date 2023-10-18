a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(a+b)

elif operator == "-":
    print(a-b)

elif operator == "*":
    print(a*b)
    
elif operator == "/":
    print(a/b)

else:
    print("Invalid operator")
