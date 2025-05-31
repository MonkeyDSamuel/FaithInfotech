#LIST
#Collection of data which are normally related related instead of storing these as separate variables
students_age=[18,21,23,20,21]
print(students_age)
print(students_age[0])
print(students_age[-1])     #access from the back
print(students_age[2:4])    #slicing the list and printing
print(students_age[:4])     #slicing from first index to the (4-1)th index
students_age.append(30)
print(students_age)

#Inserting an element at a specific position
students_age.insert(2,45)
print(students_age)

#Removing an element from list
students_age.remove(30)
print(students_age)

#Removing an element from the end
students_age.pop()
print(students_age)

#len to find the number of elements/items in the list
print(len(students_age))

#in: checks if an item is in a list or not
MyList=['h','e','l','l','o']
print('e' in MyList)

#extend(): combines 2 lists
MyList1 = ['h','e','l','l','o']
MyList2 = [1,2,3,4]
MyList1.extend(MyList2)
print(MyList1)

#reverse(): Reverses the items in a list
MyList1.reverse()
print(MyList1)

#sort(): Sorts items alphabetically or numerically
MyList.sort()
print(MyList)

#Concatenate a list
MyList3 = ['h','e','l','l','o']
print(MyList3 + ['W','o','r','l','d'])

#Duplicate a list to a number of times
print(MyList3*3)