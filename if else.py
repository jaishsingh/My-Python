import math
n=int(input("Enter the number:"))
if n%2==1:
    print("Weird")
    
elif n%2==0 & 2<=n<=5: 
    print("Not Weird")
    
elif n%2==0 & 6<=n<=20:
    print("Weird")
    
elif n%2==0 & n>20:
    print("Not Weird")           