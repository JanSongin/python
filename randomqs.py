import random
"""
#52
ran = random.randint(1,100)
print(ran)

#53
ranfruit = random.randint(0,4)
fruit = ["apple","banana","orange","tomato","watermelon"]
print(fruit[ranfruit])

#54
user = input("heads or tails (h,t) ")
ht = random.choice("ht")
if (user == ht):
    print("You win")
else:
    print("Bad luck")

#55
ranint = random.randint(1,5)
inp = int(input("Enter a number 1 to 5 "))
if(ranint == inp):
    print("Well done")
else:
    if(ranint > inp):
        inp = int(input("Try a bigger number "))
    else:
        inp = int(input("Try a smaller number "))
    if(ranint == inp):
        print("Correct")
    else:
        print("You lose")

#56
ran = random.randint(1,10)
user = int(input("Guess the number from 1 to 10 "))
while(ran != user):
    user = int(input("Try a diffrent number "))
print("Well done you guess it")

#57
ran = random.randint(1,10)
user = int(input("Guess the number from 1 to 10 "))
while(ran != user):
    if(ran > user):
        user = int(input("Try a larger number "))
    else:
        user = int(input("Try a smaller number "))
print("Well done you guess it")

#58
r = 5
points = 0
print("Welcome to my maths quiz")
while (r > 0):
    r = r - 1
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    statment = "What is " + str(num1) + " + " + str(num2) + ": "
    user = int(input(statment))
    if(user == num1 + num2):
        print("You got it right")
        points = points + 1
    else:
        print("Wrong answer")
print("You got",points,"questions right")
"""
#59