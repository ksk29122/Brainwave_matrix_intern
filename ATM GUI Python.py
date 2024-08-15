#Interface for ATM 
def mwdc(): #money withdrawl via card (function)
    atmcrd=int(input("*Press 1 to* Insert Your Debit/Credit Card: "))
    while True:
        if atmcrd==1: 
            setpass=int(input("Set your 4-digit Passcode: "))
            entpass=int(input("Enter your 4-digit Passcode: "))
            if entpass==setpass:
                widamt=int(input("Enter Amount To Withdraw In Rupees(₹): "))
                print("Withdrawl Successful!")
                break
            else:
                print("Wrong Passcode!")
                break
            return
        else:
            print("Wrong Input! Please Return To Main Screen.")
            break
        return
    
def cmw(): # Cardless money withdrawl(function)
    int(input("Enter your registered mobile number"))
    new_mpin=int(input("Set your MPIN"))
    re_mpin=int(input("Enter your MPIN"))
    while True:
        if new_mpin==re_mpin:
            print("21G6h")
            ph=input("  Enter The Characters Displayed for Human Verification:")
            if ph=="21G6h":
                widamt=int(input("Enter Amount To Withdraw In Rupees(₹): "))
                print("Withdrawl Successful")
                break
            
            else:
                print("Verification Failed!")
                break
            return
        else:
            print("Passwords mismatch")
            break
        return
    
    
    
# Main Code for calling
print("1. Money Withdrawl via Debit/ Credit")
print("2. Cardless Money withdrawl")
print("3. Customer Care")
print("4. Exit")
opt=int(input("Please Select Any Option in Numbers: "))
while True:  
    if opt==1:
        mwdc()
        break
    
    elif opt==2:
        cmw()
        break
    elif opt==3:# the number used here is invalid and dummy number
        print("Call On Toll Free Customer Care Number: +011-99999999")
        break
    elif opt==4:
        print("Thank You For Trusting Us, Your money is safe with us! ")
        break
    else:
        print("Please enter valid option")
        break
   
           
        

