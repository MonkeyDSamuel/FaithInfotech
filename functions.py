#functions
# If the same block of code is reused repeatedly, a function allows the programmer to write the block of code once, name the block and use the code as many times as needed by calling the block by name.
# Functions can read in values and return values to perform tasks including complex calculations.
# A function is named, resusable block of code that performs a task when called.
# Defining a function:
# A function is defined using the def keyword. The first line contains def followed by the function name() and a colon.
# A function must be defined before a function is called.
# Benefits of using functions:
# A function promotes modularity by putting code statements related to single task in a separate group.
# The body of a function can be executed repeatedly with multiple function calls so a function promotes reusability.

# Function to add 2 numbers:
def findsum(a,b):
    sum = a+b
    return sum
firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
result = findsum(firstnum,secondnum)
print(result)

#function to check if the number is odd or even
def oddeven(a):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
num = int(input("Enter the number to check if odd or even: "))
oddeven(num)

# Create a function to find the largest of 2 numbers(with and without user input)
# With user input:
def largest(a,b):
    if a>b:
        largest = a
        print(largest,"is the largest")
    elif b>a:
        largest = b
        print(largest,"is the largest")
    else:
        print("Both are equal")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

largest(num1,num2)

#without user input
largest(12,24)

# variable scope:
# Any variable declared inside a function is only accessible within a function. These are known as local variables.
# Any variable declared outside a function is known as global variable and it is accessible anywhere within a program.

message1 = "I am global variable"
def my_function():
    print("\nInside the function")
    #global variables are accessible inside a function
    print(message1)
    #declaring a local variable
    message2 = "I am a local variable"
    print(message2)

my_function()
print("\nOutside the function")

#global variables are accessible outside the function, my_function
print(message1)

#local variables are not accessible outside the function
# print(message2)

# Create a function that declares a local variable x = 10 and prints it. Also try printing x outside of the function and what happens?
# x appears undefined outside of the function
def trial():
    x = 10
    print(x)
trial()
print(x)