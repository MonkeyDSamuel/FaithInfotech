# 1. Write a program that converts the follwing strings to lowercase:
#     Animals
#     Badger
#     Honey Bee
#     Honey Badger

print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honey Badger".lower())


# 2. Repeat exercise 1 but convert each string to UPPERCASE instead of lower case

print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honey Badger".upper())

# 3. Write a program that removes whitespace from the following strings then print out the strings with whitespace removed
#     string1 = "   Fillet Mignon"
#     string2 = "Brisket   "
#     string3 = "   cheeseburger   "

string1 = "   Fillet Mignon"
string2 = "Brisket   "
string3 = "   cheeseburger   "
print(string1.replace(" ",""))
print(string2.strip())
print(string3.strip())

# 4. Write a program that prints out the result of .startswith("be") on each of the following strings
#     string1 = "Becomes"
#     string2 = "becomes"
#     string3 = "BEAR"
#     string4 = " beautiful"

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " beautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# 5. Using the 4 strings from exercise 4, write a program that uses string methods to alter each string so that .startswith("be") returns TRUE for all of them.

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " beautiful"
string1 = string1.lower()
string3 = string3.lower()
string4 = string4.strip()
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# 6. Create a string and print it's length

name="Samuel"
print(len(name))

# 7. Create 2 strings, concatenate them and print the result

string1 = "Hello,"
string2 = " How are you?"
print(string1+string2)