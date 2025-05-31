# A loop is a code block that returns a set of statements while a given condition is TRUE
# A loop is often used for performing a repeating task


# for loop:
# In Python a container can be a range of numbers, a string of characters or a list of values. To access objects within a container, an iterative loop can be designed to retrieve objects one at a time.
# A for loop iterates over all elements in a container.
# for loop executes a bloack of code repeatedly until the condition in the for statement is no longer valid.

fruits = ["apple","oranged","banana","cherry"]
for fruit in fruits:        #fruit here is an Iterating variable
    print(fruit)
# range() function: A for loop can be used for iteration and counting. The range() function is a common approach for implementing counting in a for loop
# A rabge() function genrates a sequence of intergers between the 2 numbers given a step size. This integer sequence is inclusive of the start and exclusive of the end of the sequence.

# range(2,6)      #2,3,4,5
# range(start,stop,step) 
#print all integers multiples of 5 less than 50

for i in range(0,50,5):
    print(i)

#To print the even numbers from the list
numbers = [12,3,7,14,10,5]
for i in numbers:
    if i%2==0:
        print(i)

# scores = [50,60,70,80]
# Write a loop and add 10 to each number in the list and print the list
scores = [50,60,70,80]
ind = 0
for i in scores:
    scores[ind] = i+10
    ind = ind+1
print(scores)

# While loop:
# A while loop is a code construct that runs a set of statements known as the loop body while a given condition known as the lopp expression is TRUE.
# At each iteration, once the loop statement is executed, the loop expression is evaluated again. If TRUE, the loop body will execute atleat one more time. If FALSE, the loop's execution will terminate and the next statement after the loop body will be executed.

#Counting with a while loop:
#A while loop can be used to count up or down. A counter variable can be used in the loop expression to determine the number of iterations executed. The change in the counter's value in each iteration is called the step size. The step size can be any positive or negative value. If the step size is a positive number, the counter counts in ascending order and if the step size is a negative number, the counter counts in descending order.
# While loop repeatedly executes instructions inside the loop while a certain condition remains valid.

for i in range(20,1,-1):
    print(i)

#print numbers from 1 to 5 using while loop
i=1
while(i<6):
    print(i)
    i = i+1

# Write a program that prints numbers from 1 to 20 using a while loop

i=1
while(i<=20):
    print(i)
    i = i+1

# Print all even numbers from 2 to 20 using a while loop

i=2
while(i<=20):
    print(i)
    i = i+2

# Use a while loop to count down from 10 to 1, then print "GO"

i=10
while(i<=10) and (i!=0):
    print(i)
    i = i-1
print("GO")

# break:
# A break statement is used within a for or a while lopp to allow the program execution to exit the loop once a given condition is triggered.
# This statement can be use to improve runtime efiiciency

for num in range(1,10):
    if num == 5:
        break
    print(num)

# continue:
# A continue statement allows for skipping the execution of the reminder of the loop without exiting the loop entirely.
# A continue statement can be used in a for or a while loop after the continue statements' execution, the loop expression will be evaluated again and the loop will continue from the loop's expression.
# A continbue statement facilitates the loop's control and readability
for num in range(1,6):
    if num==3:
        continue
    print(num) 