class LibraryMember:
    total_active_members=0
    borrowing_limit=3
    def __init__(self,name):
        self.name=name
        self.books_borrowed=0
        LibraryMember.total_active_members+=1
    def borrow_books(self,book_title):
        if not LibraryMember.book_title_is_valid(book_title):
            print(f"INVALID BOOK TITLE {book_title}")
            return
        if self.books_borrowed < LibraryMember.borrowing_limit:
            self.books_borrowed+=1
            print(f"{self.name} BORROWED {book_title}")
        else:
            print(f"{self.name} CANNOT BORROW MORE BOOKS YOUR BORROWING LIMIT REACHED!")
    @classmethod
    def updating_borrowing_limit(cls,new_limit):
        cls.borrowing_limit=new_limit
    @staticmethod
    def book_title_is_valid(title):
        return isinstance(title,str) and 1<=len(title)<=100
member1=LibraryMember("MURALI")
member2=LibraryMember("KUMAR")
print("TOTAL ACTIVE MEMBERS:",LibraryMember.total_active_members)
print()
print("BEFORE UPDATING BORROWING LIMIT:")
print()
member1.borrow_books("PYTHON PROGRAMMING")
member2.borrow_books("GAME OF THRONES")
member2.borrow_books("STRANGER THINGS")
member2.borrow_books("HOW TO KILL A MEN")
member2.borrow_books("HOW TO BECOME AN ENGINEER")
LibraryMember.updating_borrowing_limit(5)
print()
print("AFTER UPDATING BORROWING LIMIT:")
print()
member1.borrow_books("ARTIFICIAL INTELLIGENCE")
member1.borrow_books("GENERAL KNOWLEDGE")
member1.borrow_books("DATA STRUCTURES")
member1.borrow_books("HOW TO LEARN GOOD THINGS")
print()
print("BOOK TITLE VALIDATION:")
print(LibraryMember.book_title_is_valid("PYTHON PROGRAMMING"))
print(LibraryMember.book_title_is_valid(" "))
print(LibraryMember.book_title_is_valid(123))

