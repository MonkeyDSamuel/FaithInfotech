#Dictionary is a collection of related data pairs
#Dictionary keys must be unique in one dictionary

#dictionary to store the name  and age of students
mystudents = {"Abhi":30, "Samuel":23, "Allwym":22, "Alan":27}
fruit_prices = {"apple":2.5, "banana":1.2, "orange":3.0, "mango":4.5}

#access the price of orange
print("price of orange:",fruit_prices["orange"])

#add a new fruit
fruit_prices["grapes"]=2.8

print(fruit_prices)

#update the price of banana
fruit_prices["banana"]=2.5
print("updated price:\n",fruit_prices)

#remove mango
del fruit_prices["mango"]
print("updated dictionary:\n",fruit_prices)

#Get():returns value of given key
print(fruit_prices.get("banana"))

#items(): returns a list of dictionary's pairs as tuples
print(fruit_prices.items())

#keys(): returns a list of dictionary's keys
print(fruit_prices.keys())

#values(): returns a list of dictionary's values
print(fruit_prices.values())

#in:    to check if an item is present in the dictionary
print("grapes" in fruit_prices)

#len(): to get the length of the dictionary
print(len(fruit_prices))

#clear():   Deletes all of the items in the dictionary
fruit_prices.clear()

#del:       deletes the entire dictionary
del fruit_prices