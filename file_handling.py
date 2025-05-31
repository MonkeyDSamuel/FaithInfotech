# Python supports file handling and allows users to handle read and write on files along with many other file handling options. 
# The important function for working with files in python is with open. The open function takes 2 parameters, file name and mode. 
# There are 4 different modes for opening a file,
# 1. "r" - Read - Default value. Opens a file for reading, error if a file doesn't exist
# 2. "a" - Append - Opens a file for appending, creates the file if it doesn't exist.
# 3. "w" - Write - Opens a file for writing, creates the file if it doesn't exist. 
# 4. "x" - Create - Creates the specified file, returns an error if the file exists. 

# To open a file for reading, specify the name of the file.
myfile = open(r"C:\Users\ajm26\OneDrive\Desktop\CAMP1\my_file.txt","r")     # use r before typing file path to make it a raw path
print("\n",myfile.read(11))

# To udpate a file's contents at the end of the file
myfile = open(r"C:\Users\ajm26\OneDrive\Desktop\CAMP1\my_file.txt","a")
myfile.write(". Here's the new content, Mr. Samuel Thomas Mathew S.")

# To replace a content of a file with this(over-write a file)
myfile = open(r"C:\Users\ajm26\OneDrive\Desktop\CAMP1\my_file.txt","w")
myfile.write("Here's the replaced content, Mr. Samuel Thomas Mathew S.")

# TO create a new file at the specified path
myfile = (r"C:\Users\ajm26\OneDrive\Desktop\CAMP1\hello.txt","x")