class Book:
    def __init__(self, name, rollno, marks)  ->None:
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def get_info(self)  ->str: 
        info=f'''
        name:{self.name}
        rollno:{self.rollno}
        marks:{self.marks}'''
        return info
    
student1=Book(name="Rohit Singh",rollno=21,marks=97)
student2=Book(name="Shivang Singh",rollno=22,marks=98)

str1=student1.get_info()
str2=student2.get_info()


print(str1)
print(str2) 