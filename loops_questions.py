# 1. Keep asking the user to type the password, "password123" until they get it right
check=True
while(check):
    password = input("Enter the password: ")
    if password=="password123":
        print("The password is correct")
        check=False

# 2. The secret number is 9. Ask the user until they get it right

check=True
while(check):
    password = input("Enter the password: ")
    if password=="9":
        print("The password is correct")
        check=False


# 3. Print each letter in the word, "banana".

for i in "banana":
    print(i)

# 4. Write a program to swap 2 variables

a = input("Enter the first string: ")
b = input("Enter the second string: ")
c = a
a = b
b = c
print(a)
print(b)

# 5. Write a program to check if a number is prime or not

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
# 6. Write a program to find the maximum number in a list.

numbers = [1,2,32,543,32]
largest = 0
for i in numbers:
    if largest==0:
        largest = i
    else:
        if i>largest:
            largest = i
print(largest)

# 7. Write a program to find the maximum number in a list.

numbers = [1,2,32,543,32]
smallest = 0
for i in numbers:
    if smallest==0:
        smallest = i
    else:
        if i<smallest:
            smallest = i
print(smallest)

# 8. Write a program to find the middle element in a list.

numbers = [1,2,32,543,32]
mid = len(numbers)//2
middle = numbers[mid]
print(middle)