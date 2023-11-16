# Question 16(a)
# Name and School: 

#K78 E635
#66 E644
import random
while (1 == 1 ):
    s_name=input("Enter your surname:      ")    
    f_name=input("Enter your first name:   ")
    age = int(input("Enter you age:           "))
    eircode = input("Enter your Eircode:      ")
    print("Do you agree to enrol in a vaccine trail?")
    trail = input("Type 'Yes' or 'No'    ")
    if (age < 49):
        vaccine = "MRNA"
    else:
        vaccine = "ADENO"
    if (trail == "Yes"):
        vaccine = random.choice("abc")
    code = int(eircode[-1])
    code = code % 2
    if (code == 0):
        location = "Eastwood"
    elif(code == 1):
        location = "Northfield"
        print("Hello", f_name, s_name ,"you are",age ,"years old")
    print("Eircode is",eircode)
    print("You must attend",location,"for your vaccine")
    if(trail != "Yes"):
        print(f_name,"you will receive the",vaccine,"vaccine")
    elif(trail == "Yes"):
        print("You are now enrolled in the trail to receive Super vaccine",vaccine)
    print("If you have finished entering people's details type")
    again = input("'End',otherwise press RETURN: ")
    if (again == "END"):
        break


