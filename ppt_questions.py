# CODE TO SORT A PART OF THE THE LIST
index = int(input("Enter the index value: "))
string = input("Enter the list with spaces: ")
my_list = string.split()
new_list = []
new1_list = []
for x in my_list[index:]:
    new_list.append(x)      #new list appending values from old list
new_list.sort()
print(new_list)
for x in my_list[0:index]:      #setting up for loop with index
    new1_list.append(x)
full_list = new1_list+new_list
print(full_list)        #printing full list