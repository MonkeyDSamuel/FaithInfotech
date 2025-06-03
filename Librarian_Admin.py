# Librarian (Admin)

# 1. Add a new book:
#         Write a python function to add a new book.
#         The book ID should be a 5-digit random number. Ask the user to enter the book name, Author, Category, Price and Total copies, then store them in a dictionary.

# 2. Update book details:
#         Write a function that takes a Book ID as input and allowsthe librarian to update the price and number of copies.
#         If the Book ID does not exist, display: "Book ID not found!!"

# 3. Delete a book:
#         Write a function that deletes a book from books dictionary based on the Book ID. If the Book ID isn't found, show an error message.

# 4. View all books:
#         Write a function that loops through the books dictionary and displays the list of all books in a readable format.

# 5. View specific book's details:
#         Ask for a Book ID and show the book's full details.
#         If the ID doesn't exist, print: "Book ID not found"

# 6. Add a new member:
#         Write a python function to add a new library member.
#         The member ID should be a 4-digit random number.
#         Ask for the member name, mobile number, and email ID, and initialize borrowed as an empty list.
     
# 7. View all members:
#         Write a function to deplay all members' details including their borrowed book ID's

# 8.Borrow a book:
#         Write a function where a member enters their member IDand a Book ID to borrow a book.
#         Check if the copies are available.
#         If yes, reduce the copies by one and add the Book ID to the member's borrowed list.
#         If no copies are available, print: "Book not available rn"

# 9.Return a book:
#         Write a function that allows a member to return a borrowed book using their member ID and Book ID.
#         Increase the number of copies by 1.
#         Remove the Book ID from the member's borrowed list.

# 10.View borrowed books:
#         Write a function that takes a member ID and displays the list of borrowed Book IDs and their corresponding book names

import random

members = {}
books = {}
def Add_Book():
    book_ID = random.randint(10000,99999)
    if book_ID in books:
        print("-------BOOK ALREADY EXISTS-------")
    else:
        print(f"BOOK ID: {book_ID}")
        name = input("Enter the name of the book: ")
        author = input("Enter the name of the book's author: ")
        category = input("Enter the name of the book's category: ")
        try:
            price = int(input("Enter the book's price: "))
            copies = int(input("Enter the number of book's copies: "))
            books[book_ID]={"name":name, "author": author,"category":category,"price":price,"copies":copies}
        except:
            print("-------PRICE CAN ONLY BE IN INTEGER VALUES-------")

def Update_Book():
    print("-------SELECT THE BOOK TO BE UPDATED FROM THE LIST BELOW-------")
    for book_ID in books:
        print(f"BOOK ID: {book_ID}")
    book_ID = int(input("Enter the Book ID from the list above to update:"))
    if book_ID in books:
        try:
            price = int(input(f"UPDATED BOOK'S PRICE:[{books[book_ID]["price"]}]" or books[book_ID]["price"]))
            copies = int(input(f"UPDATED BOOK'S COPIES:[{books[book_ID]["copies"]}]" or books[book_ID]["copies"]))
            books[book_ID]={"price":price,"copies":copies}
        except:
            print("-------PRICE CAN ONLY BE IN INTEGER VALUES-------")
    else:
        print("-------THE BOOK ID YOU HAVE ENTERED DOESN'T EXIST-------")

def Del_Book():
    print("-------SELECT THE BOOK TO BE DELETED FROM THE LIST BELOW-------")
    for book_ID in books:
        print(f"BOOK ID: {book_ID}")
    try:
        book_ID = int(input("Enter the Book ID from the list above to delete:"))
        if book_ID in books:
            del books[book_ID]
        else:
            print("Book ID you have entered doesn't exist")
    except:
        print("-------BOOK ID CAN ONLY BE IN INTEGER VALUES-------")

def View_All_Book():
    print("-------ALL BOOKS LIST-------")
    if not books:
        print("-------BOOKS AREN'T THERE IN LIBRARY-------")
    else:
        for book_ID in books:
            print(f"\nBOOK ID: {book_ID}")
            print(f"BOOK'S NAME: {books[book_ID]["name"]}")
            print(f"BOOK'S AUTHOR NAME: {books[book_ID]["author"]}")
            print(f"BOOK'S CATEGORY NAME: {books[book_ID]["category"]}")
            print(f"BOOK'S PRICE: {books[book_ID]["price"]}")
            print(f"BOOK'S COPIES: {books[book_ID]["copies"]}\n")

def View_Book():
    print("-------SELECT THE BOOK TO BE VIEWED FROM THE LIST BELOW-------")
    for book_ID in books:
        print(f"BOOK ID: {book_ID}")
    book_ID = int(input("Enter the Book ID from the list above to delete:"))  
    if not books:
        print("-------BOOKS AREN'T THERE IN LIBRARY-------")
    else:
        print(f"\nBOOK ID: {book_ID}")
        print(f"BOOK'S NAME: {books[book_ID]["name"]}")
        print(f"BOOK'S AUTHOR NAME: {books[book_ID]["author"]}")
        print(f"BOOK'S CATEGORY NAME: {books[book_ID]["category"]}")
        print(f"BOOK'S PRICE: {books[book_ID]["price"]}")
        print(f"BOOK'S COPIES: {books[book_ID]["copies"]}\n")

def Add_Mem():
    mem_ID = random.randint(1000,9999)
    if mem_ID in members:
        print("-------MEMBER ALREADY EXISTS-------")
    else:
        print(f"MEMBER ID: {mem_ID}")
        borrowed = []
        name = input("Enter the name of the member: ")
        mob = input("Enter the mobile number of the member: ")
        email = input("Enter the email ID of the member: ")
        members[mem_ID]={"name":name, "mob": mob,"email":email,"borrowed":borrowed}

def View_All_mem():
    print("-------ALL MEMBERS LIST-------")
    if not members:
        print("-------MEMBERS AREN'T THERE IN LIBRARY-------")
    else:
        for mem_ID in members:
            print(f"\nMEMBER'S ID: {mem_ID}")
            print(f"MEMBER'S NAME: {members[mem_ID]["name"]}")
            print(f"MEMBER'S MOBILE NUMBER: {members[mem_ID]["mob"]}")
            print(f"MEMBER'S EMAIL ID: {members[mem_ID]["email"]}")
            print(f"MEMBER'S BORROWED BOOKS: {members[mem_ID]["borrowed"]}\n")

def Bor_Book():
    print("-------SELECT THE MEMBER FROM THE LIST BELOW-------")
    for mem_ID in members:
        print(f"MEMBER ID: {mem_ID}")
    mem_ID = int(input("Enter the member ID from the list above:"))
    print("-------SELECT THE BOOK TO BE BORROWED FROM THE LIST BELOW-------")
    for book_ID in books:
        print(f"BOOK ID: {book_ID}")
    book_ID = int(input("Enter the book ID from the list above:"))
    borrow = []
    if books[book_ID]["copies"]!=0:
        copies = books[book_ID]["copies"]
        borrow = members[mem_ID]["borrowed"]
        borrow.append(book_ID)
        copies = copies - 1
        members[mem_ID]["borrowed"] = borrow
        books[book_ID]["copies"] = copies
    else:
        print("-------BOOK IS NOT AVAILABLE TO BORROW-------")

def Ret_Book():
    print("-------SELECT THE MEMBER FROM THE LIST BELOW-------")
    for mem_ID in members:
        print(f"MEMBER ID: {mem_ID}")
    mem_ID = int(input("Enter the member ID from the list above:"))
    print("-------SELECT THE BOOK TO BE RETURNED FROM THE LIST BELOW-------")
    borrow = []
    borrow = members[mem_ID]["borrowed"]
    for book_ID in borrow:
        print(f"BOOK ID: {book_ID}")
    book_ID = int(input("Enter the book ID from the list above:"))
    count = 0
    copies = books[book_ID]["copies"]
    if not borrow:
        print("-------NO BOOKS PRESENT-------")
    else:
        for i in borrow:
            if i==book_ID:
                del borrow[count]
                copies = copies + 1
                members[mem_ID]["borrowed"] = borrow
                books[book_ID]["copies"] = copies
            
            else:
                count = count + 1
    
def View_Bor_Book():
    print("-------SELECT THE MEMBER FROM THE LIST BELOW TO VIEW BORROWED BOOK-------")
    for mem_ID in members:
        print(f"MEMBER ID: {mem_ID}")
    mem_ID = int(input("Enter the member ID from the list above:"))
    print(f"MEMBER ID: {mem_ID}")
    borrow = members[mem_ID]["borrowed"]
    if not borrow:
        print("-------NO BOOKS PRESENT-------")
    else:
        for i in borrow:
            print(f'BORROWED BOOK ID:{i} BORROWED BOOK NAME: {books[i]["name"]}')
def Menu():
    while True:
        print("-------SELECT YOUR CHOICE ADMIN-------")
        print("\n1. ADD A NEW BOOK")
        print("\n2. UPDATE BOOK DETAILS")
        print("\n3. DELETE A BOOK")
        print("\n4. VIEW ALL BOOKS")
        print("\n5. VIEW SPECIFIC BOOK'S DETAILS")
        print("\n6. ADD A NEW MEMBER")
        print("\n7. VIEW ALL MEMBERS")
        print("\n8. BORROW A BOOK")
        print("\n9. RETURN A BOOK")
        print("\n10. VIEW ALL BORROWED BOOKS")
        print("\n11. EXIT PROGRAM")

        choice = int(input("Enter your choice in numbers:"))
    
        if choice == 1:
            Add_Book()
        elif choice == 2:
            Update_Book()
        elif choice == 3:
            Del_Book()
        elif choice == 4:
            View_All_Book()
        elif choice == 5:
            View_Book()
        elif choice == 6:
            Add_Mem()
        elif choice == 7:
            View_All_mem()
        elif choice == 8:
            Bor_Book()
        elif choice == 9:
            Ret_Book()
        elif choice == 10:
            View_Bor_Book()
        elif choice == 11:
            print("-------PROGRAM EXITED SUCCESSFULLY-------")
            break
        else:
            print("-------INVALID CHOICE.... THE CHOICE MUST BE NUMBERS FROM (1 to 7)-------")

Menu()