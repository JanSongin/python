import random
"""
#118
num = int(input("Enter a number "))
def sub(a):
    a = num + 1
    print(a)
sub(num)

#119

#def rand():
low = int(input("Enter a low number "))
high = int(input("Enter a high number "))
comp_int = random.randint(low,high)
#return comp_int
#rand()
guess = int(input("I am thinking of a number guess it "))
while (guess != comp_int):
    if (guess > comp_int):
        guess = int(input("Your guess is larger than the number try again "))
    elif (guess < comp_int):
        guess = int(input("Your guess is smaller than the number try again "))
print("You did it the number was",comp_int)

#120
print("1)  Addition")
print("2) Subtraction")
choice = int(input("Enter 1 or 2: "))
if (choice == 1):
    n1 = random.randint(5,20)
    n2 = random.randint(5,20)
    string = "Add "+str(n1)+" and "+str(n2)+" together: "
    choice2 = int(input(string))
    n1 = n1 + n2
    if (choice2 == n1):
        print("Well done your not stupid")
    else:
        print("Your stupid the answer was",n1)
elif (choice == 2):
    n1 = random.randint(25,50)
    n2 = random.randint(1,25)
    string = "Take away "+str(n2)+" from "+str(n1)+" : "
    choice2 = int(input(string))
    n1 = n1 - n2
    if (choice2 == n1):
        print("Well done your not stupid")
    else:
        print("Your stupid the answer was",n1)
    
else:
    print("Your stupid I asked for 1 or 2 not",choice)
"""
#121
namelist = []
while (0 == 0):
    print("1: Add name")
    print("2: Change name")
    print("3: Delete name")
    print("4: View all names")
    print("5: End programe")
    choice = int(input("Enter 1 to 5: "))
    if (choice == 1):
        namelist.append(input("Enter the name you want to add: "))
    elif(choice == 2):
        print("):")
    elif(choice == 3):
        print("):")
    elif(choice == 4):
        print("):")
    elif(choice == 5):
        break