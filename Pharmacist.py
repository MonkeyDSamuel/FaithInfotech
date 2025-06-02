# 3. Pharmacist:
# ○ Responsibilities:
#   ■ Medicine Management: The pharmacist is responsible for managing
#   medicines in the clinic. This includes:
#       ■ Add new medicine.
#       ■ View all medicines available.
#       ■ Search for a particular medicine.
#       ■ Update details of a medicine.
#       ■ Delete a medicine record.
#       ■ Login Required: Pharmacists will have a login feature to access the
#         system.

medicines = {}

username = "Samuel"
password = "Hello"

# LOGIN FUNCTION
def Login():
    print("-------WELCOME DEAR PHARMACIST-------")
    u_name = input("Enter the username of the pharmacist: ")
    pwd = input("Enter the password of the pharmacist: ")
    if(u_name=="" or pwd==""):
        print("-------PLEASE ENTER YOUR LOGIN CREDENTIALS-------")
        return False
    elif(u_name == username and pwd == password and u_name!="" and pwd!=""):
        print("-------LOGIN SUCCESSFUL-------")
        return True
    else:
        print("-------INVALID CREDENTIALS-------")
        return False
    
# FUNCTION TO ADD MEDICINE
def Add_med():
    print("-------MEDICINE DETAILS-------")
    try:
        med_ID = int(input("Enter the ID of the medicine:"))
        if med_ID in medicines:
            print("MEDICINE ALREADY EXISTS IN THE PHARMACY")
        else:
            name = input("Enter the name of the medicine: ")
            company = input("Enter the company name of the medicine: ")
            generic_name = input("Enter the generic name of the medicine: ")
            price = int(input("Enter the price of the medicine: "))
            medicines[med_ID] = {"name":name, "company":company, "generic_name":generic_name, "price":price}
    except:
        print("PLEASE ENTER THE APPROPRIATE VALUES")
# FUNCTION TO DELETE MEDICINE FROM THE LIST
def Del_med():
    print("-------MEDICINE DELETION FROM PHARMACY-------")
    try:
        med_ID = int(input("Enter the ID of the medicine:"))
        if med_ID in medicines:
            del medicines[med_ID]
        else:
            print("-------INVALID MEDICINE ID-------THE MEDICINE DOES NOT EXIST-------")
    except:
        print("PLEASE INPUT INTEGER VALUES FOR MED ID")
# FUNCTION TO UPDATE MEDICINE DETAILS
def Upd_med():
    print("-------MEDICINE DETAILS UPDATION-------")
    try:
        med_ID = int(input("Enter the ID of the medicine:"))
        if med_ID in medicines:
            name = input(f"NEW MEDICINE NAME[{medicines[med_ID]["name"]}]: " or medicines[med_ID]["name"])
            company = input(f"NEW COMPANY NAME[{medicines[med_ID]["company"]}]: " or medicines[med_ID]["company"])
            generic_name = input(f"UPDATED GENERIC NAME[{medicines[med_ID]["generic_name"]}]: " or medicines[med_ID]["generic_name"])
            price = int(input(f"NEW UPDATED PRICE[{medicines[med_ID]["price"]}]: " or medicines[med_ID]["price"]))
            medicines[med_ID] = {"name":name, "company":company, "generic_name":generic_name, "price":price}
        else:
            print("-------MEDICINE ID NOT FOUND-------")
    except:
        print("PLEASE INPUT THE APPROPRIATE VALUES")
# FUNCTION TO SEARCH FOR MEDICINE USING ID
def Search_med():
    print("-------MEDICINE SEARCH FROM PHARMACY-------")
    try:
        med_ID = int(input("Enter the ID of the medicine:"))
        if med_ID in medicines:
            print("-------MEDICINE FOUND-------")
            print(f"MEDICINE NAME: {medicines[med_ID]["name"]}")
            print(f"COMPANY NAME: {medicines[med_ID]["company"]}")
            print(f"GENERIC NAME: {medicines[med_ID]["generic_name"]}")
            print(f"PRICE: {medicines[med_ID]["price"]}")
        else:
            print("-------MEDICINE NOT FOUND-------")
    except:
        print("PLEASE THE APPROPRIATE VALUES")

# FUNCTION TO VIEW ALL MEDICINES FROM THE LIST
def View_med():
    if not medicines:
        print("NO MEDICINES ARE AVAILABLE")
    else:
        print("-------LIST OF ALL MEDICINES FROM PHARMACY-------")
        for med_ID in medicines:
            print(f"MEDICINE NAME: {medicines[med_ID]["name"]}")
            print(f"COMPANY NAME: {medicines[med_ID]["company"]}")
            print(f"GENERIC NAME: {medicines[med_ID]["generic_name"]}")
            print(f"PRICE: {medicines[med_ID]["price"]}")

# MENU FUNCTION TO START AFTER LOGIN IS VALID
def Menu():
    while True:
        print("\n1. Add new medicine")
        print("\n2. Delete a medicine record")
        print("\n3. Update details of a medicine")
        print("\n4. Search for a particular medicine")
        print("\n5. View all medicines available")
        print("\n6. LOG OUT") 

        choice = input("Enter the numbered choice:")

        if choice=="1":
            Add_med()
        elif choice=="2":
            Del_med()
        elif choice=="3":
            Upd_med()
        elif choice=="4":
            Search_med()
        elif choice=="5":
            View_med()
        elif choice=="6":
            print("-------LOGGED OUT SUCCESSFULLY-------")
            break
        else:
            print("-------INVALID CHOICE-------")

if Login():
    Menu()