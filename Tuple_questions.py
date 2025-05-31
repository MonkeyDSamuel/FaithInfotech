# 1. Create a Tuple of 4 countries and print it

countries = ("India","USA","UK","China")
print(countries)

# 2. print the second and last item

print(countries[1],countries[3])

# 3. print the first 2 items

print(countries[:1])

# 4. Concatenate 2 tuples, one of numbers and one of fruits

numbers = (1,2,3,4)
fruits = ("orange","mango","pineapple","banana")
print(numbers+fruits)

# 5. Convert a list, [1,2,3] into a tuple

List1 = [1,2,3]
Tuple1 = tuple(List1)
print(Tuple1)

# 6. Check if "India" is in the Tuple

print("India" in countries)

# 7. Find the length of a Tuple

print(len(countries))
print(len(fruits))
print(len(numbers))
print(len(Tuple1))

# 8. Delete a Tuple using del

del countries,fruits,numbers,Tuple1