import time
import os


print("Countdown")
i=int(input('enter the time limit:'))
while(i>0):
    print(i)
    time.sleep(1)
    i=i-1
    os.system('cls')
   
    
    
print("You can proceed further")