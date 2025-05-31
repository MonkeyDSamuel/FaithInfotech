#Student Management system
#login credentials - Use  a username and password
username = "admin"
password  ="1234"

#Creating an empty dictionary, students
students = {}

#Login function
def Login():
    print("-------STUDENT MANAGEMENT SYSTEM LOGIN-------")
    u_name = input("Username: ")
    pwd = input("Password: ")
    if(u_name==username and pwd==password):
        print("LOGIN SUCCESSFUL")
        return True
    else:
        print("INVALID CREDENTIALS")
        return False

#Add Student details   
def Add_Student():
    roll = input("Enter the student's roll number:")
    if roll in students:
        print("......Student already exists......")
        return
    name = input("Enter the student's name:")
    class_name = input("Enter the student's class:")
    ph_no = input("Enter the student's phone number:")
    students[roll] = {"name":name, "class":class_name, "Phone_number":ph_no}
    print("-------Student added successfully-------")

#Editing Student's details
def Edit_Student():
    roll = input("Enter the student's roll number:")
    if roll in students:
        print("Enter new details:......(Leave empty to keep current value)")
        name = input(f"New name[{students[roll]["name"]}]") or students[roll]["name"]
        class_name = input(f"New Class[{students[roll]["class"]}]") or students[roll]["class"]
        ph_no = input(f"New Phone number[{students[roll]["Phone_number"]}]") or students[roll]["Phone_number"]
        students[roll] = {"name":name, "class":class_name, "Phone_number":ph_no}
        print("Student Updated")
    else:
        print("Student not found")

#Delete Student
def Del_Student():
    roll = input("Enter the student's roll number:")
    if roll in students:
        del students[roll]
        print("Student deleted")
    else:
        print("Student not found")

#Search Student
def Search_student():
    roll = input("Enter the student's roll number:")
    if roll in students:
        print("-------Student Found-------")
        print("Name: ", students[roll]["name"])
        print("Class: ", students[roll]["class"])
        print("Phone Number: ", students[roll]["Phone_number"])
    else:
        print("Student not found")

#List Students
def List_students():
    if not students:
        print("Students not found")
    else:
        print("-------Students List-------")
        for roll in students:
            print("Roll Number:", roll)
            print("Name: ", students[roll]["name"])
            print("Class: ", students[roll]["class"])
            print("Phone Number: ", students[roll]["Phone_number"])

def Menu():
    while True:
        print("\n1. Add Student")
        print("\n2. Edit Student")
        print("\n3. Delete Student")
        print("\n4. Search Student")
        print("\n5. List Students")
        print("\n6. Exit")

        choice = input("Enter your Choice:")


        if choice=="1":
            Add_Student()
        elif choice == "2":
            Edit_Student()
        elif choice == "3":
            Del_Student()
        elif choice == "4":
            Search_student()
        elif choice == "5":
            List_students()
        elif choice == "6":
            print("Exiting the system")
            break
        else:
            print("------INVALID CHOICE, PLEASE TRY AGAIN------")

if Login():
    Menu()