# Create a library management system in python. The system should support Login functionality and allow performing CRUD operationson books
# Requirements:
# 1. Login system:
#       Predefined username and password
# 2. Menu after Login:
#    After successful login, show a menu
#         Add book
#         view all books
#         Update book 
#         Delete book 
#         Search Book 
#         Exit 
# 3. Each book should have:
#         BookId(Unique)
#         Title
#         Author
#         Year
#         NumberOfCopies

username = "Samuel"
password  ="1234"

books = {}

def Login():
    print("-------LIBRARY MANAGEMENT SYSTEM LOGIN-------")
    u_name = input("Username: ")
    pwd = input("Password: ")
    if(u_name==username and pwd==password):
        print("LOGIN SUCCESSFUL")
        return True
    else:
        print("INVALID CREDENTIALS")
        return False

def Add_Book():
    BookId = input("Enter the Book ID:")
    if BookId in books:
        print("......Book Already exists......")
        return
    title = input("Enter the Book's Title:")
    author = input("Enter the Author's name:")
    year = input("Enter the year of publishing:")
    copies = input("Enter the number of copies released:")
    books[BookId] = {"title":title, "author":author, "year":year, "copies":copies}
    print("-------Book details added successfully-------")

def Edit_Book_Details():
    BookId = input("Enter the Book ID:")
    if BookId in books:
        print("Enter new details:......(Leave empty to keep current value)")
        title = input(f"New Title[{books[BookId]["title"]}]") or books[BookId]["title"]
        author = input(f"New Author[{books[BookId]["author"]}]") or books[BookId]["author"]
        year = input(f"New year of Publication[{books[BookId]["year"]}]") or books[BookId]["year"]
        copies = input(f"New number of copies[{books[BookId]["copies"]}]") or books[BookId]["copies"]
        books[BookId] = {"title":title, "author":author, "year":year, "copies":copies}
        print("Book Details Updated")
    else:
        print("Book not found")

def Del_Book():
    BookId = input("Enter the Book ID:")
    if BookId in books:
        del books[BookId]
        print("Book details removed from Library")
    else:
        print("Book not found")

def Search_Book():
    BookId = input("Enter the Book ID:")
    if BookId in books:
        print("-------Book Found-------")
        print("Book's Title: ", books[BookId]["title"])
        print("Book's Author: ", books[BookId]["author"])
        print("Book's Year of Publication: ", books[BookId]["year"])
        print("Number of Copies released: ", books[BookId]["copies"])
    else:
        print("Book not found") 

def View_Books():
    if not books:
        print("Books not found")
    else:
        print("-------Books List-------")
        for BookId in books:
            print("Book's Title: ", books[BookId]["title"])
            print("Book's Author: ", books[BookId]["author"])
            print("Book's Year of Publication: ", books[BookId]["year"])
            print("Number of Copies released: ", books[BookId]["copies"])

def Menu():
    while True:
        print("\n1. Add Book")
        print("\n2. Edit Book Details")
        print("\n3. Delete Book from Library")
        print("\n4. Search Book")
        print("\n5. List Books")
        print("\n6. Exit")

        choice = input("Enter your Choice:")


        if choice=="1":
            Add_Book()
        elif choice == "2":
            Edit_Book_Details()
        elif choice == "3":
            Del_Book()
        elif choice == "4":
            Search_Book()
        elif choice == "5":
            View_Books()
        elif choice == "6":
            print("Exiting the system")
            break
        else:
            print("------INVALID CHOICE, PLEASE TRY AGAIN------")

if Login():
    Menu()