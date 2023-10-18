def find_sum(*number):
    result=0
    
    for num in number:
        result=result+num
        
    print('sum=',result)
        
        
        
find_sum(int(input('val1:')),int(input('val2:')),int(input('val3:')))