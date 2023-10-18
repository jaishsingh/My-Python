percentage=int(input("Enter the percentage value:"))
if(percentage<=34):
    print('fail')
    
elif(percentage>=35 and percentage<=50):
    print('pass')
    
elif(percentage>=51 and percentage<=60):
    print('second division pass')
    
elif(percentage>=61 and percentage<=80):
    print('1st division')
    
elif(percentage>=81 and percentage<=95):
    print('class topper')
    
elif(percentage>=96 and percentage<=100):
    print('unbeliveable')
    
elif(percentage>100):
    print('error')