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


def Login():
    print("-------WELCOME DEAR PHARMACIST-------")
    u_name = input("Enter the username of the pharmacist: ")
    pwd = input("Enter the password of the pharmacist: ")
    if(u_name == username and pwd == password):
        print("-------LOGIN SUCCESSFUL-------")
        return True
    else:
        print("-------INVALID CREDENTIALS-------")
        return False
    
def Add_med():
    print("-------MEDICINE DETAILS-------")
    med_ID = int(input("Enter the ID of the medicine:"))
    if med_ID in medicines:
        print("MEDICINE ALREADY EXISTS IN THE PHARMACY")
    else:
        name = input("Enter the name of the medicine: ")
        company = input("Enter the company name of the medicine: ")
        year = input("Enter the year of manufacture: ")
        qty = input("Enter the quantity of the medicine:")
        medicines[med_ID] = {"name":name, "company":company, "year":year, "qty":qty}

def Del_med():
    print("-------MEDICINE DELETION FROM PHARMACY-------")
    med_ID = int(input("Enter the ID of the medicine:"))
    if med_ID in medicines:
        del medicines[med_ID]
    else:
        print("-------INVALID MEDICINE ID-------THE MEDICINE DOES NOT EXIST-------")

def Upd_med():
    print("-------MEDICINE DETAILS UPDATION-------")
    med_ID = int(input("Enter the ID of the medicine:"))
    if med_ID in medicines:
        name = input(f"NEW MEDICINE NAME[{medicines[med_ID]["name"]}]" or medicines[med_ID]["name"])
        company = input(f"NEW COMPANY NAME[{medicines[med_ID]["company"]}]" or medicines[med_ID]["company"])
        year = input(f"UPDATED YEAR[{medicines[med_ID]["year"]}]" or medicines[med_ID]["year"])
        qty = input(f"NEW UPDATED QUANTITY[{medicines[med_ID]["qty"]}]" or medicines[med_ID]["qty"])
        medicines[med_ID] = {"name":name, "company":company, "year":year, "qty":qty}
    else:
        print("-------MEDICINE ID NOT FOUND-------")

def Search_med():
    print("-------MEDICINE SEARCH FROM PHARMACY-------")
    med_ID = int(input("Enter the ID of the medicine:"))
    if med_ID in medicines:
        print("-------MEDICINE FOUND-------")
        print(f"MEDICINE NAME: {medicines[med_ID]["name"]}")
        print(f"NEW COMPANY NAME: {medicines[med_ID]["company"]}")
        print(f"UPDATED YEAR: {medicines[med_ID]["year"]}")
        print(f"NEW UPDATED QUANTITY: {medicines[med_ID]["qty"]}")
    else:
        print("-------MEDICINE NOT FOUND-------")

def View_med():
    if not medicines:
        print("NO MEDICINES ARE AVAILABLE")
    else:
        print("-------LIST OF ALL MEDICINES FROM PHARMACY-------")
        for med_ID in medicines:
            print(f"MEDICINE NAME: {medicines[med_ID]["name"]}")
            print(f"NEW COMPANY NAME: {medicines[med_ID]["company"]}")
            print(f"UPDATED YEAR: {medicines[med_ID]["year"]}")
            print(f"NEW UPDATED QUANTITY: {medicines[med_ID]["qty"]}")
def Menu():
    while True:
        print("1. Add new medicine")
        print("2. Delete a medicine record")
        print("3. Update details of a medicine")
        print("4. Search for a particular medicine")
        print("5. View all medicines available")
        print("6. LOG OUT") 

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