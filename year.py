year=int(input("year"))
if year % 4==0 &(year % 100!=0 or year%400==0):
     print("Leap year")
else:
    print("Not leap year")