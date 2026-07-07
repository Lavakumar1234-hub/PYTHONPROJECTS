class Book:
    total_books=0
    def __init__(self,title,author):
        if not Book.is_valid_title(title):
            raise ValueError("Title must have at least 3 characters")
        self.title=title
        self.author=author
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split(",")
        title=title.strip()
        author=author.strip()
        if not cls.is_valid_title(title):
            raise ValueError("Title must have at least 3 characters")
        return cls(title,author)
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
book1=Book("A Game of Thrones","George R.R.Martin")
book2=Book("Wings of Fire","A.P.J. Abdul Kalam")
book3=Book.from_string("Harry Potter,J.K.Rowling")
book4=Book.from_string("Python,Guido Van Rossum")
print(book1.title,"-",book1.author)
print(book2.title,"-",book2.author)
print(book3.title,"-",book3.author)
print(book4.title,"-",book4.author)