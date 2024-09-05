#Inventory Management System
#Use stock.txt for storing the values
#Dictionaries
unit_price={}
description={}
stock={}
cart=[]

#Open file with stock
details = open("stock.txt","r")
no_items  = int((details.readline()).rstrip("\n"))

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

c='y'#Abbreviation for YES wherever needed

#Instructions
print("****************************************")
print("Welcome to Inventory Management System")
print("****************************************")
print("A-Add an item")
print("D-Delete item from inventory")

print("E-Edit specifics of an item")
print("L-List all items")
print("I-Inquire about a product")
print("P-Purchase")
print("C-Checkout")
print("S-Show all products purchased")
print("R-Remove an item from Cart")
print("Q-Quit")
print("help-See all commands again")
print()


total_cost=0 
flag=0 


while(c!= "q" or c!= "Q"):
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"): # To Exit the program
        break
        
    elif(c=="A" or c=="a"):#Add a product
        p_no = int(input("Enter Serial number: "))
        p_pr = float(input("Enter product price: "))
        p_desc = input("Enter product description: ")
        p_stock = int(input("Enter product quantity: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(p_no in unit_price):
                p_no+=1
                m=1
        if(m==1): #Change Serial no. to the closest possible if the entered serial no. already exists
            print()
            print("Serial number already exists! changing value to ",p_no)
                
        unit_price.update({p_no: p_pr})
        description.update({p_no: p_desc})
        if(p_stock > -1):
            stock.update({p_no: p_stock})
        else:
            p_stock = 0
            stock.update({p_no: p_stock})
            print("Value can't be negative, the stock has been set to 0.")
        print()
        print("Serial number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
        print("Product added successfully!")
        print()
        
    elif(c=="E" or c=="e"):#Edit a product
        print()
        p_no = int(input("Enter serial number: "))
        if(p_no in unit_price):
            p_pr = float(input("Enter product price: "))
            p_desc = input("Enter product description: ")
            p_stock = int(input("Enter product stock: "))
                
            unit_price.update({p_no: p_pr})
            description.update({p_no: p_desc})
            stock.update({p_no: p_stock})
            
        else:
            print("Item not found! Add an item use a")
        print()

    elif(c=="L" or c=="l"):#Show all the product
        print()
        print("Product : price: ",unit_price)
        print("Descriptions: ",description)
        print("Stock left of Item: ",stock)
        print("****************************************")

    elif(c=="I" or c=="i"):#Information of aa existing product
        print()
        p_no=int(input("Enter Serial Number: "))
        if(p_no in unit_price):
            print()
            print("Serial number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
            if(stock.get(p_no)<3 and stock.get(p_no)!=0):
                print("Only ",stock.get(p_no)," remaining! Low Stock Alert!!!")
            print()
        else:
            print("Item not found!")
            print()
        
    elif(c=="P" or c=="p"):#Purchase a product
        print()
        p_no = int(input("Enter serial number: "))
        if(p_no in unit_price):
            if(flag==1):
                flag=0
            stock_current = stock.get(p_no)
            if(stock_current>0):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current-1
                item_price = unit_price.get(p_no)
                total_cost = total_cost+item_price
                print(description.get(p_no),"added to cart: ","₹",item_price)
                cart.append(p_no)
            else:
                print("Currently Unavailable!")
        else:
                print("Item not found!")
        print()
        
    elif(c=="C" or c=="c"):#Check out
        print()
        print("Your Cart: ",cart)
        print("Total: ","₹",round(total_cost,2))
        tax= round(0.13*total_cost,2)
        print("Tax is 13%: ","₹",tax)
        total = round(total_cost+tax,2)
        print("After Tax: ","₹",total)
        total_cost=0
        flag=1
        print("*******************************")
        print("Continue Shopping!, Quit: q")
        print("*******************************")

    elif(c=="D" or c=="d"):#Delete from inventory
        print()
        p_no = int(input("Enter Serial number: "))
        if(p_no in unit_price):
            are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
            if(are_you_sure=="y" or are_you_sure=="Y"):
                unit_price.pop(p_no)
                description.pop(p_no)
                stock.pop(p_no)
                print("Item successfully removed!")
                print("**************************************")
        else:
            print("Item not found!")
            print("*****************************************")
            
    elif(c=="help"):#Costumer Care (Dummy Number)
        print("*****************************")
        print("Help Centre")
        print("*****************************")
        print("For complaint: +011-11110000. ")
    elif(c=="R" or c=="r"):#To remove an item from the cart
        print()
        are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
        if(are_you_sure=="y"):
            p_no = int(input("Enter serial number to remove from cart: "))
            if(p_no in cart):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current+1
                item_price = unit_price.get(p_no)
                total_cost = total_cost-item_price
                j=0
                for i in range(0,len(cart)):#To find the index of the product in the list cart
                    if(i==p_no):
                        j=i

                cart.pop(j)
                print(description.get(p_no),"removed from cart: ")
                print()
            else:
                print()
                print("Item not in cart!")
                print()
                
    elif(c=="s" or c=="S"):
        print()
        print(cart)
        print()
        
    else:
        print()
        print("ERROR! Choose a valid option!")
        print()


#Total if the user quits without checking out
if(total_cost>0 and flag==0):
    print()
    print("You bought: ",cart)
    print("Total: ","₹",round(total_cost,2))
    tax= round(0.13*total_cost,2)
    print("Tax is 13%: ","₹",tax)
    total = round(total_cost+tax,2)
    print("After Tax: ","₹",total)
    
print()
print("Thank you for using Inventory Management System")

#Write the updated inventory to the file
details = open("stock.txt","w")
no_items=len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+description[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
    
details.close()
