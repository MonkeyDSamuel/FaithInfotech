# 1. Create a list of 5 fruits and print it:
#     fruits=['apple','banana','cherry','mango','orange']

fruits=['apple','banana','cherry','mango','orange']
print("These are the list of fruits:")
print(fruits)

# 2. Access the 3rd item fromn the list

print(fruits[2])

# 3. Change the third item of the list to grapes

fruits.insert(2,'grapes')
print(fruits)

# 4. Add "kiwi" to the end of the list

fruits.append('kiwi')
print(fruits)

# 5. Insert "pineapple" at the second position

fruits.insert(1,'pineapple')
print(fruits)

# 6. Remove "banana" from the list

fruits.remove('banana')
print(fruits)

# 7. Print the first 3 items of the list

print(fruits[0:3])

# 8. Check if 'apple' is in the list

print('apple' in fruits)

# 9. Sort the list in ascending order

fruits.sort()
print(fruits)

# 10.Reverse the list

fruits.reverse()
print(fruits)