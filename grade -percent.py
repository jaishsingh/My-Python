marks=int(input('Enter the marks:'))
if  marks<=34 and marks>=0:
    print('fail')
elif marks>=35 and marks<=59:
    print('grade= C')
elif marks>=60 and marks<=79:
    print('grade= B')
elif marks>=80 and marks<=89:
    print('grade= A')
elif marks>=90 and marks<=100:
    print('grade= A+')
else:
    print('error')