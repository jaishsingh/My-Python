def outer():
    message_1=str(input('enter the string 1:'))
    message_2=str(input('enter the string 2:'))
    def inner():
        nonlocal message_1
        print('inner',message_1)
        
    inner()
    print('outer',message_2)
outer()
        