# Question 16(a)
# Student Name:

#This program is a simple ordering system
print("Welcome to the new online ordering system.\n")

total_cost=0
item_count=0
name = input("Please enter your user name: ")
amount = int(input("How many items are in the customers order: "))
if (amount < 0):
    print("Invalid option")
    
else:
    while (amount > 0):
        item_count = item_count + 1
        price_of_item=float(input("Enter the price of item {}".format(item_count)+" : € "))
        total_cost+=price_of_item
        amount = amount - 1

    print("You entered",item_count,"items and the total is €",total_cost)
    balance = float(input("What is the customers current account balance € "))
    balance = balance - total_cost
    if (balance >= 0):
        print("Your remaining balance: €", balance)
    else:
        balance = balance - (balance*2)
        balance = round(balance,2)
        print("The customer does not have enough credit in their account, they still owe: €",balance)
    print("The member of staff  who processed your order was:", name)