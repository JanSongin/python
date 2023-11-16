import random
while(1 == 1):
    print("1: play")
    print("2: end")
    ran = random.randint(1,3)
    i = int(input("Enter 1 or 2: "))
    if(i = 1):
        user = input("Rock, paper, scissors? ")
        if(user == "rock" and ran == 2):
            print("You win")
        elif(user == "paper" and ran == 3):
            print("You win")
        elif(user == "scissors" and ran == 1):
            print("You win")
        elif(user == "rock" and ran == 1):
            print("Draw")
        elif(user == "paper" and ran == 2):
            print("Draw")
        elif(user == "scissors" and ran == 3):
            print("Draw")
        elif(user == "rock" and ran == 3):
            print("You lose")
        elif(user == "paper" and ran == 1):
            print("You lose")
        elif(user == "scissors" and ran == 2):
            print("You lose")
        else:
            print("error")
    else:
        break