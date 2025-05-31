#count method returns the number of times the substring appears in the string

#count the entire string
print("hello Good morning".count('d'))

#count from index 3 to end of the string
print("hello Good morning".count('d',3))

#endswith - return TRUE if the string ends with the specified suffix
print("Superman".endswith("man"))   #TRUE

#check from index 3 to end of the string
print("Superman".endswith("man",3)) #TRUE

#check from index 2 to 6-1
print("Superman".endswith("man",2,6))   #FALSE

#isalnum() returns TRUE if all the characters in the strings contain alphabets and digits
print("hello1234".isalnum())    #TRUE

print("h e l l o 1234".isalnum())   #FALSE

#isalpha() checks if all characters in a string are only letters
print("hellogoodmorning".isalpha()) #TRUE

print("Hello Good morning".isalpha())   #FALSE: Because it contains spaces other than alphabets

print("hellogoodmorning123".isalpha())  #FALSE: Because it contains numbers other than alphabets

print("hellogoodmorning!?".isalpha()) #FALSE: Because it contains special symbols other than aplhabets

#isdigit checks if all characters in a string are digits
print("31243254125415".isdigit())   #TRUE

print("123QABC".isdigit())  #FALSE

#islower() checks if all letters are lower case
print("helloiamsamuel".islower())   #TRUE

print("hello1234".islower())    #TRUE as it checks only letters

print("ALSIPasilgfsdnmfhb".islower())   #FALSE as it has both uppercase and lower case letters

#isupper() checks if all letters are UPPER CASE
print("HELLO".isupper())    #TRUE

print("Hello".isupper())    #FALSE as it contains lower case letters too

#join(): Parameter provided is joined by a separator
separator = '-'
MyTuple = ("hello")
print(separator.join(MyTuple))

#replace() is used to replace the path of a string with something else
#string.replace(old,new)
print("Superman".replace("man","girl"))

#len() is used to get the length of the string or the number of characters of the string
message="Hello,I am Samuel"
print(len(message))
