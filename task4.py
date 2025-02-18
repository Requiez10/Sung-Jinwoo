class Book:
    def __init__(self, title, author, year_published):
        
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        
        return f"\nTitle: {self.title}, Author: {self.author}, Year Published: {self.year_published}"


book1 = Book(" Jujutsu Kaisen, Vol. 1 ", "Gege Akutami", 2018 )
book2 = Book(" Naruto, Vol. 1 ", "Masashi Kishimoto", 2000 )
book3 = Book(" One Piece, Vol. 1: Romance Dawn ", "Eiichiro Oda ", 1997 )


print(book1.describe())
print(book2.describe())
print(book3.describe())
