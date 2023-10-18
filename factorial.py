num=int(input("Enter the number:"))
fact=1
for x in range (1,num+1):
    fact=fact*x

print("The factorial of {} is {}".format(num,fact))    
