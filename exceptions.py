# Mistakes in programs are called errors. There are 2 types of errors.
# 1. Syntax errors
# 2. Logical errors
# Syntax error occurs when you write code that isn't allowed in the python language
# Errors that happe nwhen the program is running are called exceptions.
# Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.
# Errors detected during execution are called "exceptions".

# try block: try to run teh code.
# except: what to do if an error happens.
# finally: runs all the time.
# The genral syntax is:
''' try:
        do something
    except:
        do something else when an error occurs
'''

try:
    age = int(input("Enter your age:"))
    print("Your age is", age)
except:
    print("Please enter numbers only")

try:
    number = int(input("Enter the number to divide 10: "))
    result = 10/number
    print("Result: ",result)
except:
    print("Something went wrong")

# Ask the user to enter the item name
# show the price
# handle the case when the item doesn't exist in the cart

try:
    cart = {"Apple":30,"Banana":20,"Milk":50}
    item_name = input("Enter the item name: ")
    print("Price: ",cart[item_name])
except:
    print("Item doesn't exist")

# We can use variables to represent a string:

# Using f-string(f stands for format), python formats the string by replacing the nam,e of any variable in braces with its value.

# Place the letter f immediately before the opening quotation mark

first_name = "Sam"
last_name = "leo"

full_name = f"{first_name} {last_name}"