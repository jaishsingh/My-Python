# # list literal
# fruits = ["apple", "mango", "orange"] 
# print(fruits)

# # tuple literal
# numbers = (1, 2, 3) 
# print(numbers)

# # dictionary literal
# alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
# print(alphabets)

# # set literal
# vowels = {'a', 'e', 'i' , 'o', 'u'} 
# print(vowels)

# x = 5
# y = 2
# print('The value of x is {} and y is {}'.format(x,y))

'''Input  swipe the number'''
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
temp = num1
num1 = num2
num2 = temp
print('value of num1 is {} and value of num2 is {}'.format(num1,num2))
print('Type of data',type(num1))