# 1. Admin:
#   ○ Responsibilities:
#       ■ Staff Management: The admin is responsible for managing the clinic's
#       staff, including the following actions:
#       ■ Add a new staff member.
#       ■ View all staff details.
#       ■ Search for a particular staff member.
#       ■ Update details of an existing staff member.
#       ■ Delete staff member.
#       ■ Login Required: Admin will have a login feature to access the system.
#       ■ A staff dictionary could store staff details like staff_id,
#       name,designation,dateOfjoining,location,salary,age,phoneNumber etc.



staff = {}

username = "Samuel"
password = "Hello"

# LOGIN FUNCTION
def Login():
    print("-------WELCOME DEAR ADMIN-------")
    u_name = input("Enter the username of the ADMIN: ")
    pwd = input("Enter the password of the ADMIN: ")
    if(u_name=="" or pwd==""):
        print("-------PLEASE ENTER YOUR LOGIN CREDENTIALS-------")
        return False
    elif(u_name == username and pwd == password and u_name!="" and pwd!=""):
        print("-------LOGIN SUCCESSFUL-------")
        return True
    else:
        print("-------INVALID CREDENTIALS-------")
        return False
    
# FUNCTION TO ADD STAFF
def Add_staff():
    print("-------STAFF DETAILS-------")
    try:
        staff_ID = int(input("Enter the ID of the staff:"))
        if staff_ID in staff:
            print("-------STAFF ALREADY EXISTS IN THE CLINIC-------")
        else:
            name = input("Enter the name of the staff: ")
            age = int(input("Enter the age of the staff: "))
            designation = input("Enter the designation of the staff: ")
            date = input("Enter the date of joining of the staff: ")
            salary = int(input("Enter the salary of the staff: "))
            location = input("Enter the location of the staff's residence: ")
            staff[staff_ID] = {"name":name, "age":age, "designation":designation, "date":date, "location":location ,"salary":salary}
    except:
        print("-------PLEASE ENTER THE APPROPRIATE VALUES-------")
# FUNCTION TO DELETE STAFF FROM THE LIST
def Del_staff():
    print("-------STAFF DELETION FROM CLINIC-------")
    try:
        staff_ID = int(input("Enter the ID of the staff:"))
        if staff_ID in staff:
            del staff[staff_ID]
        else:
            print("-------INVALID STAFF ID-------THE STAFF DOES NOT EXIST-------")
    except:
        print("-------PLEASE INPUT INTEGER VALUES FOR MED ID-------")
# FUNCTION TO UPDATE STAFF DETAILS
def Upd_staff():
    print("-------STAFF DETAILS UPDATION-------")
    try:
        staff_ID = int(input("Enter the ID of the staff:"))
        if staff_ID in staff:
            name = input(f"NEW STAFF NAME[{staff[staff_ID]["name"]}]: " or staff[staff_ID]["name"])
            age = input(f"NEW age[{staff[staff_ID]["age"]}]: " or staff[staff_ID]["age"])
            designation = input(f"UPDATED designation[{staff[staff_ID]["designation"]}]: " or staff[staff_ID]["designation"])
            date = input(f"UPDATED DATE OF JOINING OF STAFF[{staff[staff_ID]["date"]}]" or staff[staff_ID]["date"])
            location = input(f"UPDATED RESIDENCE LOCATION OF STAFF[{staff[staff_ID]["location"]}]" or staff[staff_ID]["location"])
            salary = int(input(f"NEW UPDATED salary[{staff[staff_ID]["salary"]}]: " or staff[staff_ID]["salary"]))
            staff[staff_ID] = {"name":name, "age":age, "designation":designation, "date":date, "location":location ,"salary":salary}
        else:
            print("-------STAFF ID NOT FOUND-------")
    except:
        print("-------PLEASE INPUT THE APPROPRIATE VALUES-------")
# FUNCTION TO SEARCH FOR staff USING ID
def Search_staff():
    print("-------STAFF SEARCH FROM CLINIC-------")
    try:
        staff_ID = int(input("Enter the ID of the staff:"))
        if staff_ID in staff:
            print("-------STAFF FOUND-------")
            print(f"STAFF NAME: {staff[staff_ID]["name"]}")
            print(f"AGE: {staff[staff_ID]["age"]}")
            print(f"DESIGNATION: {staff[staff_ID]["designation"]}")
            print(f"DATE OF JOINING: {staff[staff_ID]["date"]}")
            print(f"LOCATION: {staff[staff_ID]["location"]}")
            print(f"SALARY: {staff[staff_ID]["salary"]}\n")
        else:
            print("-------STAFF NOT FOUND-------")
    except:
        print("-------PLEASE ENTER THE APPROPRIATE VALUES FOR STAFF ID-------")

# FUNCTION TO VIEW ALL staff FROM THE LIST
def View_staff():
    if not staff:
        print("-------NO STAFF ARE AVAILABLE-------")
    else:
        print("-------LIST OF ALL STAFF FROM PHARMACY-------")
        for staff_ID in staff:
            print(f"STAFF ID: {staff_ID}")
            print(f"STAFF NAME: {staff[staff_ID]["name"]}")
            print(f"AGE: {staff[staff_ID]["age"]}")
            print(f"DESIGNATION: {staff[staff_ID]["designation"]}")
            print(f"DATE OF JOINING: {staff[staff_ID]["date"]}")
            print(f"LOCATION: {staff[staff_ID]["location"]}")
            print(f"SALARY: {staff[staff_ID]["salary"]}\n")

# MENU FUNCTION TO START AFTER LOGIN IS VALID
def Menu():
    while True:
        print("\n1. ADD NEW STAFF")
        print("\n2. DELETE A STAFF RECORD")
        print("\n3. UPDATE DETAILS OF A STAFF")
        print("\n4. SEARCH FOR A PARTICULAR STAFF")
        print("\n5. VIEW ALL STAFF AVAILABLE")
        print("\n6. LOG OUT\n") 

        choice = input("Enter the numbered choice:")

        if choice=="1":
            Add_staff()
        elif choice=="2":
            Del_staff()
        elif choice=="3":
            Upd_staff()
        elif choice=="4":
            Search_staff()
        elif choice=="5":
            View_staff()
        elif choice=="6":
            print("\n-------LOGGED OUT SUCCESSFULLY-------\n")
            break
        else:
            print("\n-------INVALID CHOICE-------\n")

if Login():
    Menu()