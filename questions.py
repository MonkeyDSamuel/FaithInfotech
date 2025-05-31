# Print all the numbers from 1 to 100 using loop

for i in range(1,101):
    print(i)

# Print the multiplication table of a number entered by the user(*)

num = int(input("Enter the number to produce it's multiplication table: "))
for i in range(1,11):
    result = num*i
    print(num,"x",i,"=",result)

# Calculate the factorial of a number using while loop

num = int(input("Enter the number to find it's factorial: "))
fact = 1
while(num!=0):
    fact = num*fact
    num = num-1
print("Factorial of",num,"is:",fact)

# Print all even numbers between 1 and 50

for i in range(2,50,2):
    print(i)

# Find the sum of digits of a number (*)

num = int(input("Enter the number to find the sum of its digits: "))
result = 0
while(num!=0):
    result = result + num%10
    num = num//10
print(result)

# Write a function that takes a number and returns whether it is prime or not

a = int(input("Enter the number to check: "))
flag = True
if(a==2):
    flag = True
for i in range(2,a):
    if(a%i==0):
        print(a,"is not a prime number")
        flag = False
        break
if(flag):
    print(a,"is a prime number")

# Write a function that calculates the area of a circle

def Circle(rad):
    area = rad*rad*3.14
    return area
rad = float(input("Enter the radius of the circle: "))
area = Circle(rad)
print("The area of the circle is:",area)

# Write a function that takes in 2 numbers and returns their greatest Common Divisor

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
greatest=0
if num1>num2:
    large = num1
else:
    large = num2
while(large!=0):
    if(num2%large==0 and num1%large==0):
        if(greatest<large):
            greatest = large
    large = large-1
print("The Greatest Common Divisor is",greatest)


# Write a function that counts how many vowels are there in a string (*)


def vowel_check(string):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    count = 0
    for i in string:
        if i in vowels:
            count = count + 1
    print("Number of vowels:",count)
string = input("Enter the string to find the vowels in it: ")
vowel_check(string)

# Write a function to reverse a string (*)

def reverse_string(new_string):
    print(new_string[::-1])

string = input("Enter the string to be reversed: ")
reverse_string(string)
 
# Write a program that divides 2 numbers and handles division by zero

try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1/num2
    print("Result: ",result)
except:
    print("Division by zero not possible, the second number you've entered is zero")

#Ask the user to enter their age and handle the case where they type the text instead of a number

try:
    age = int(input("Enter your age:"))
    print("Your age is", age)
except:
    print("Please enter numbers only")