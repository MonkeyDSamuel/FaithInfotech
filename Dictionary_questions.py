# 1. Create a dictionary called cities with the following data:
#     "Chennai":"Tamil Nadu"
#     "Mumbai":"Maharashtra"
#     "Benagaluru":"Karnataka"

cities = {"Chennai":"Tamil Nadu", "Mumbai":"Maharashtra", "Benagaluru":"Karnataka"}

# 2. print the state of Mumbai

print(cities.get("Mumbai"))

# 3. Check if delhi is in the dictionary, if not, add "Delhi":"Delhi" to the dictionary

print("Delhi" in cities)
cities["Delhi"]="Delhi"

# 4. Update mumbai's value to "Mumbai":"Maharashtra(West India)"

cities["Mumbai"]="Maharashtra(West India)"
print(cities)

# 5. print all of the city names

print(cities.keys())

# 6. print all of the state names

print(cities.values())

# 7. print all of the city pairs

print(cities.items())

#print how many cities are in the dictionary

print(len(cities))