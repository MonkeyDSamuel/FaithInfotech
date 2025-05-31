#CONDITIONALS STATEMENTS

# A condition is an expression that evaluates TRUE or FALSE
# An if statement is a decision making structure that contains a condition and a body of statements.  If the condition is TRUE, the body is executed and if the condition is FALSE, the body isn't executed.
# An if statement defines actions to be performed when a condition is TRUE. An else statement is used with an if statement and contains a body of statements that is executed when the if statement's condition is FALSE


age = int(input("Enter the age of the individual: "))
if(age>=18):
    print("You're an adult")
else:
    print("ACCESS DENIED")

#Check whether a number is positive
num = int(input("Enter the number to check: "))
if(num>=0):
    print("It is positive")
else:
    print("It is negative")

#Write a program to check whether a number is odd or even:
num1 = int(input("Enter the number: "))
if(num1%2==0):
    print("The number entered is even")
else:
    print("The number entered is odd")


#Take 2 numbers from the user and print which one's greater:

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if(a>b):
    print(a,"is the largest")
else:
    print(b,"is the largest")

#Ask the user for their age if they are 18 or older, print, "You are eligible to vote", if not, "You are not eligible to vote":

age = int(input("Enter the age of the individual: "))
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Sometime, a complicated decision is based on more than a single condition.
# Chaining decision statements with elif allows the programmer to check for multiple conditions
# An elif(short for else if) statment checks a conditionn when the prior statements condition is FALSE.
# An elif statement is a part of a train and must follow if or elif staement

marks = int(input("Enter the marks of the student:"))
if(marks>=90):
    print("GRADE A")
elif(marks>=80):
    print("GRADE B")
elif(marks>=70):
    print("GRADE C")
elif(marks>=60):
    print("GRADE D")
elif(marks>=50):
    print("GRADE E")
elif(marks>=40):
    print("PASS")
else:
    print("FAIL")


#Ask the user to input the month(1-12) and print the season:
#Winter: Dec- Feb
#Spring: Mar - May
#Summer: Jun - Aug
#Autumn: Sep - Nov

month = int(input("Enter the month(1-12): "))
if(12>=month>=2):
    print("Winter")
elif(3>=month>=5):
    print("Spring")
elif(6>=month>=8):
    print("Summer")
elif(9>=month>=11):
    print("Autumn")
else:
    print("Invalid month")

# Ask the user for the string and check if it's a vowel or a consonant

new_string = input("Enter the string:")
vowels = ['a','e','i','o','u','A','E','I','O','U']
if(new_string==vowels):
    print("It is a vowel")
else:
    print("It is a consonant")

# Ask the user to marls(0 to 100).If marks>=40, PASS else, FAIL

score = int(input("Enter the score of the student: "))
if(score>=40):
    print("PASS")
else:
    print("FAIL")

# Ask the user to enter a number and check if it's divisilble by 3 or 5
check = int(input("Enter the number to check: "))
if(check%3==0):
    print("It is divisible by 3")
elif(check%5==0):
    print("It is divisible by 5")
else:
    print("sorry")

# Ask the user for their age and print:
# child(age<13)
# Teenager(13-19)
# adult(20-59)
# senior(age>60)

age = int(input("Enter the age of the individual: "))
if(age<13):
    print("Child")
elif(13<=age<=19):
    print("Teenager")
elif(20<=age<=59):
    print("Adult")
else:
    print("Senior")

# Ask the user to enter three numbers from the user and print the greatest among them

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if(a>b):
    if(a>c):
        largest = a
    else:
        largest = c
elif(b>a):
    if(b>c):
        largest = b
    else:
        largest = c
else:
    print("All are equal")

print("The largest of all is",largest)

# Ask the user to enter 2 numbers and an operator(+,-,*,/) and perform the calculations

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("enter the operator")
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num/num2)
else:
    print("Invalid operator")