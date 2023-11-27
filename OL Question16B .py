# Question 16_b
# Student Name: 

Standard_Postal_List=["Netherlands","Denmark","Poland","Portugal","Finland","Romania","France","Germany","Greece","Spain","Hungary","Sweden","Ireland"]
ask = input("Please enter the country that you wish to send the order to: ")
if(Standard_Postal_List.count(ask) >= 1):
    print("This country uses standard postage and packaging costs.")
else:
    print("This country is not on the approved delivery list.")
    extend = input("Would you like to add this country to the approved Postal List for future deliveries, y/n: ")
    if (extend == "y"):
        Standard_Postal_List.append(ask)
        Standard_Postal_List.sort()
        print(ask,"has been added to the Standard Postal List")
        print(Standard_Postal_List)
    elif(extend == "n"):
        print(ask,"has not been added to the Standard Postal List")
    