
import random

customer = {}
pan = []

#-----------------------------------------------------------ADMINISTRATOR FUNCTIONS BELOW---------------------------------------------------

#   1. Adding a New Customer
#       ✓ Account No – (AutoGenerate 9 digits)
#       ✓ Customer Name
#       ✓ Account Type (Savings/Current)
#       ✓ Balance
#       ✓ Minimum Balance
#       ✓ Mobile Number
#       ✓ Email Id
#       ✓ ATM Pin (Autogenerate 4 digits)

def Add_Customer():
    print("\n-------ACCOUNT CREATION CONSOLE-------\n")
    cust_ID = random.randint(100000000,999999999)
    if cust_ID in customer:
        print("-------ACCOUNT NUMBER ALREADY EXISTS-------")
        cust_ID = random.randint(100000000,999999999)
    print(f"ACCOUNT NUMBER: {cust_ID}")
    try:
        name = input("Enter the name of the customer: ")
        if 0<len(name)<=30:      
            type = input("Enter account type(Savings/Current): ")
            balance = int(input("Enter the account balance:"))
            min_balance = int(input("Enter the account's minimum balance:"))
            mob = input("Enter the mobile number:")
            if len(mob)!=10 and mob.isdigit()==False:
                print("\nINVALID MOBILE NUMBER\n")
                return
            email = input("Enter the email_ID:")
            atm = random.randint(1000,9999)
            print(f"CUSTOMER'S ATM PIN: {atm}")
            customer[cust_ID] = {"name":name, "type":type, "balance":balance, "min_balance":min_balance, "mob":mob, "email":email, "atm":atm}
        else:
            print("\nINVALID NAME\n")
            return
    except:
        print("\nPLEASE ENTER VALID INPUT\n")
#   2. Updating Customer Details
#       ✓ Account No
#       ✓ Mobile Number (ask for new mobile number)
#       ✓ Email Id (ask for new email id)

def Upd_Customer():
    print("\n-------CUSTOMER DETAILS UPDATION CONSOLE-------\n")
    count = 1
    print("-------ACCOUNT NUMBER LIST-------")
    for cust_ID in customer:
        print(f"ACCOUNT NUMBER {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: "))
        if cust_ID in customer:
            mob = input(f"UPDATED MOBILE NUMBER: [{customer[cust_ID]["mob"]}]" or customer[cust_ID]["mob"])
            email = input(f"UPDATED EMAIL ID: [{customer[cust_ID]["email"]}]" or customer[cust_ID]["email"])
            customer[cust_ID] = {"mob":mob,"email":email}
        else:
            print("-------ACCOUNT NUMBER DOESN'T EXIST-------")
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#   3. Deleting a Customer
#       ✓ Ask for Account number to delete a Customer

def Del_Customer():
    print("\n-------CUSTOMER DETAILS DELETION CONSOLE-------\n")
    count = 1
    print("-------ACCOUNT NUMBER LIST-------")
    for cust_ID in customer:
        print(f"CUSTOMER ID {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: "))
        if cust_ID in customer:
            del customer[cust_ID]
            print("-------ACCOUNT NUMBER DELETED SUCCESSFULLY-------")
        else:
            print("-------ACCOUNT NUMBER DOESN'T EXIST-------")
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#   4. Display the list of all Customers in the Bank
#       ✓ Just show all customer details

def Display_Customer():
    if not customer:
        print("-------THERE ARE NO CUSTOMERS IN THE BANK-------")
    else:
        for cust_ID in customer:
            print(f"ACCOUNT NUMBER:{cust_ID}\n")
            print(f"NAME:{customer[cust_ID]["name"]}\n")
            print(f"ACCOUNT TYPE:{customer[cust_ID]["type"]}\n")
            print(f"ACCOUNT BALANCE:{customer[cust_ID]["balance"]}\n")
            print(f"ACCOUNT MINIMUM BALANCE:{customer[cust_ID]["min_balance"]}\n")
            print(f"MOBILE NUMBER:{customer[cust_ID]["mob"]}\n")
            print(f"EMAIL ID:{customer[cust_ID]["email"]}\n")
            print(f"ATM PIN:{customer[cust_ID]["atm"]}\n")

#   5. Display Customer Details of a specific Customer
#       ✓ Ask for Account number to display the Customer details
#       ✓ If user enters any account number which is not there in
#       our Bank we have to show “Account number not found..!!!”

def Diplay_A_Customer():
    count = 1
    print("-------ACCOUNT NUMBER DETAILS-------")
    for cust_ID in customer:
        print(f"ACCOUNT NUMBER {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: ")) 
        if cust_ID in customer:
            print(f"ACCOUNT NUMBER:{cust_ID}\n")
            print(f"NAME:{customer[cust_ID]["name"]}\n")
            print(f"ACCOUNT TYPE:{customer[cust_ID]["type"]}\n")
            print(f"ACCOUNT BALANCE:{customer[cust_ID]["balance"]}\n")
            print(f"ACCOUNT MINIMUM BALANCE:{customer[cust_ID]["min_balance"]}\n")
            print(f"MOBILE NUMBER:{customer[cust_ID]["mob"]}\n")
            print(f"EMAIL ID:{customer[cust_ID]["email"]}\n")
            print(f"ATM PIN:{customer[cust_ID]["atm"]}\n")
        else:
            print("-------ACCOUNT NUMBER DOESN'T EXIST-------")
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#----------------------------------------------------CUSTOMER MENU FUNCTIONS BELOW:-----------------------------------------------------

#   1. Depositing Money into Customer Account
#       ✓ If Amount is greater than 50k then ask the customer to
#       enter his/her PAN Card number

def Deposit():
    print("\n-------DEPOSIT WINDOW-------\n")
    print("-------ACCOUNT NUMBER LIST-------")
    count = 1      #LIST ADDED TO CHECK THE ACCOUNT NUMBER AS IT IS RANDOMLY GENERATED...
    for cust_ID in customer:
        print(f"ACCOUNT NUMBER {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: ")) 
        balance = customer[cust_ID]["balance"]
        bal = int(input("Enter the amount to be deposited:"))
        if bal>50000:
            pan = input("AMOUNT TO BE DEPOSITED IS ABOVE 50000...PLEASE ENTER YOUR PAN CARD NUMBER")
            bal = bal + balance
            customer[cust_ID]["balance"] = bal
        else:
            bal = bal + balance
            customer[cust_ID]["balance"] = bal
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#   2. Withdraw Money from Customer Account
#       ✓ First calculate Available Balance (difference of balance
#       and min balance)
#       e.g. balance is 7k min bal is 1k then available balance is 6k
#       ✓ If withdrawal amount is greater than available balance
#       then show error Message as “Insufficient funds..!!!”.
#       ✓ If Amount is greater than 50k then ask the customer to
#       enter his/her PAN Card number

def Withdraw():
    print("\n-------WITHDRAW WINDOW-------\n")
    print("-------ACCOUNT NUMBER LIST-------") 
    count = 1     #LIST ADDED TO CHECK THE ACCOUNT NUMBER AS IT IS RANDOMLY GENERATED...
    for cust_ID in customer:
        print(f"ACCOUNT NUMBER {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: ")) 
        balance = customer[cust_ID]["balance"]
        min_balance = customer[cust_ID]["min_balance"]
        avail_bal = balance - min_balance
        draw = int(input("Enter the amount to be withdrawn: "))
        if draw>avail_bal:
            print("-------INSUFFICIENT FUNDS!!-------")
        else:
            if draw>50000:
                pan = input("AMOUNT TO BE DEPOSITED IS ABOVE 50000...PLEASE ENTER YOUR PAN CARD NUMBER")
                balance = balance - draw
                customer[cust_ID]["balance"] = balance
            else:
                balance = balance - draw
                customer[cust_ID]["balance"] = balance
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#   3. Show Balance of a Customer
#       ✓ Ask for Account number to display Customer details

def View_Balance():
    count = 1
    print("-------ACCOUNT NUMBER LIST-------")      #LIST ADDED TO CHECK THE ACCOUNT NUMBER AS IT IS RANDOMLY GENERATED...
    for cust_ID in customer:
        print(f"ACCOUNT NUMBER {count}. {cust_ID}")
        count+=1
    try:
        cust_ID = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: ")) 
        if cust_ID in customer:
            print(f"ACCOUNT NUMBER:{cust_ID}\n")
            print(f"NAME:{customer[cust_ID]["name"]}\n")
            print(f"ACCOUNT TYPE:{customer[cust_ID]["type"]}\n")
            print(f"ACCOUNT BALANCE:{customer[cust_ID]["balance"]}\n")
            print(f"ACCOUNT MINIMUM BALANCE:{customer[cust_ID]["min_balance"]}\n")
            print(f"MOBILE NUMBER:{customer[cust_ID]["mob"]}\n")
            print(f"EMAIL ID:{customer[cust_ID]["email"]}\n")
            print(f"ATM PIN:{customer[cust_ID]["atm"]}\n")
        else:
            print("-------ACCOUNT NUMBER DOESN'T EXIST-------")
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")


#   4. Transferring Money from One Account to Another account
#       ✓ Ask for to Account number and amount to transfer
#       ✓ After successful transaction show message
#       “ Transferred Amount Successfully”

def Transfer():
    count = 1
    print("-------SELECT YOUR ACCOUNT NUMBER FROM THE LIST-------")      #LIST ADDED TO CHECK THE ACCOUNT NUMBER AS IT IS RANDOMLY GENERATED...
    for i in customer:
        print(f"ACCOUNT NUMBER {count}. {i}")
        count+=1
    cust_ID1 = int(input("ENTER YOUR ACCOUNT NUMBER FROM THE LIST ABOVE: ")) 
    count = 1
    print("-------TRANSFER LIST-------")      #LIST ADDED TO CHECK THE ACCOUNT NUMBER AS IT IS RANDOMLY GENERATED...
    for j in customer:
        if j == cust_ID1:
            continue
        print(f"ACCOUNT NUMBER {count}. {j}")
        count+=1
    try:
        cust_ID2 = int(input("ENTER THE ACCOUNT NUMBER FROM THE LIST ABOVE: "))
        amt = int(input("Enter the amount to be transferred:"))
        balance = customer[cust_ID1]["balance"]
        min_balance = customer[cust_ID1]["min_balance"]
        avail_bal = balance - min_balance
        if amt>avail_bal:
            print("-------TRANSFER NOT POSSIBLE-------")
        else:
            balance = balance - amt
            customer[cust_ID1]["balance"] = balance
            balance  = customer[cust_ID2]["balance"]
            balance = balance + amt
            customer[cust_ID2]["balance"] = balance
            print("\nTRANSFERRED SUCCESSFULLY\n")
    except:
        print("\n------PLEASE ENTER VALID INPUT-------\n")

#---------------------------------------------------END OF ALL ADMIN AND CUSTOMER FUNCTIONS------------------------------------------------

#----------------------------------------------------------MENU FUNCTIONS BELOW----------------------------------------------------------

def Admin_Login():
    while True:
        print("-------WELCOME ADMINISTRATOR-------")
        print("\n1. ADD A NEW CUSTOMER")
        print("\n2. UPDATE CUSTOMER DETAILS")
        print("\n3. DELETE A CUSTOMER")
        print("\n4. DISPLAY ALL CUSTOMERS IN THE BANK")
        print("\n5. DISPLAY A SPECIFIED CUSTOMER'S DETAILS")
        print("\n6. EXIT")

        try:
            choice = int(input("Enter the choice from the above options:"))

            if choice==1:
                Add_Customer()
            elif choice == 2:
                Upd_Customer()
            elif choice == 3:
                Del_Customer()
            elif choice == 4:
                Display_Customer()
            elif choice == 5:
                Diplay_A_Customer()
            elif choice == 6:
                print("-------EXITING.....-------")
                break
            else:
                print("\nINVALID OPTION.... PLEASE CHOOSE NUMBERS FROM 1-6")
        except:
            print("\n------PLEASE ENTER CHOICE-------\n")
def Customer_Login():
    while True:
        print("-------WELCOME CUSTOMER-------")
        print("\n1. DEPOSIT AMOUNT")
        print("\n2. WITHDRAW AMOUNT")
        print("\n3. VIEW BALANCE")
        print("\n4. TRANSFER AMOUNT TO ANOTHER ACCOUNT")
        print("\n5. EXIT CUTOMER LOGIN CONSOLE")

        try:
            choice = int(input("Enter the choice from the above options:"))

            if choice==1:
                Deposit()
            elif choice == 2:
                Withdraw()
            elif choice == 3:
                View_Balance()
            elif choice == 4:
                Transfer()
            elif choice == 5:
                print("-------EXITING.....-------")
                break
            else:
                print("\nINVALID OPTION.... PLEASE CHOOSE NUMBERS FROM 1-5")
        except:
            print("\n------PLEASE ENTER CHOICE-------\n")

def Menu():
    while True:
        print("-------WELCOME USER-------")
        print("\n1. ADMINISTRATOR LOGIN")
        print("\n2. CUSTOMER LOGIN")
        print("\n3. OOPS....IT WAS AN ACCIDENT....LOG OUT\n")

        try:
            choice = int(input("Enter the choice from the above options:"))

            if choice==1:
                Admin_Login()
            elif choice == 2:
                Customer_Login()
            elif choice == 3:
                print("-------LOGGING OUT.....-------")
                break
            else:
                print("\nINVALID OPTION.... PLEASE CHOOSE NUMBERS FROM 1-3")
        except:
            print("\n------PLEASE ENTER CHOICE-------\n")

#START OF EXECUTION:

Menu()

# Customer is authorized to :


