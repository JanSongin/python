"""
#1
def a(l):
    if(l == []):
        return 0
    else:
        return l[0] + a(l[1:])
numlist = [1,5,21,6,8,2,5,9,0,32,6,2,7,83,2,7,5,45,12,18]
b = a(numlist)
print(b)


#2
def a(l):
    if(l == 1):
        return l
    elif(l == 0):
        return 1
    else:
        return l * a(l - 1)
fact = int(input("What number do you want a factorial of (Between 0 and 986) "))
b = a(fact)
print(b)

#3
def fib(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
term = int(input("Which term of the Fibonacci sequence do you want "))
n = fib(term)
print(n)

#4
num = input("Input a number larger than 10 " )
def sumdigit(n):
    if (len(n) == 0):
        return 0
    else:
        return int(n[0]) + sumdigit(n[1:])
answer = sumdigit(num)
print(answer)
"""
#5


n = []
n[1] = int(input("Enter a number "))
n[2] = int(input("Enter a number "))
def gcd(n):
    
output = gcd(n)
print(output)
