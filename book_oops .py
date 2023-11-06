class Book:
    def __init__(self, title, author, year)  ->None:
        self.title=title
        self.author=author
        self.year=year

    def get_info(self)  ->str: 
        info=f'''
        Book name:{self.title}
        Author:{self.author}
        Year:{self.year}'''
        return info
    
object1=Book(title="Gulliver Travel:Part1",author="Jonathon Swift",year=1726)
object2=Book(title="Harry potter:Part1",author="J.K.Rowlin",year=1986)

str1=object1.get_info()
str2=object2.get_info()


print(str1)
print(str2)  