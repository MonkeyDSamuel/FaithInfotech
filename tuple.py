#Tuple
#Tuples are like lists but unlike lists, we can't modify their initial values. The values are enclosed within parenthesis. Syntax: List_name=('value1','value2')

months = ("jan","feb","mar","apr")
print(months[0])

#len(): to find the number of items in a Tuple
MyTuple = ("hello","world",2022)
print(len(months))
print(len(MyTuple))

#in: Checks if an item is present in a Tuple
print("hello" in MyTuple)

#Tuples are immutable that is, we can't change or remove individual elements after the tuple is created
#But on the contrary, we can delete the entire tuple using the del keyword

# del MyTuple
# print(MyTuple)

#concatenating two Tuples
MyTuple = ("hello","world",2022)
YourTuple = ("how","are","you")

print(MyTuple+YourTuple)

#Duplicate a Tuple using the * operator:
print(MyTuple*3)

# 1. Create a Tuple named languages with values: python, java and C++. Then print the tuple

languages = ("python","java","C++")
print(languages)

# 2. devices = ("laptop","tablet","smartphone","smartwatch")
#         Print the second elemennt

devices = ("laptop","tablet","smartphone","smartwatch")
print(devices[1])

#         Print the last element using negative indexing

print(devices[-1])

# 3. cities = ("Mumbai","Delhi","Chennai","Kolkata")
#         Check if Delhi is in the Tuple

cities = ("Mumbai","Delhi","Chennai","Kolkata")
print("delhi" in cities)

# 4. sports = ("cricket","football","hockey","tennis","badminton")
#         write the code to print the number of items in the tuple

sports = ("cricket","football","hockey","tennis","badminton")
print(len(sports))

# 5. Create a tuple with the value "Python" and repeat it 4 times

code = ("Python")
print(code*4)

# 6. delete the entire tuple

del languages,devices,cities,code