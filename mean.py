file = open("mean-median-mode-frequency.csv","r")
"""
count = 0
total = 0
l = 0
bob = 0
n = 0
for line in file:
    if (len(line) > 1):
        n = n + 1
        num = line.strip()
        num = num.split(",")
        while(len(num) > count):
            l = int(num[count])
            total = total + l
            count = count + 1
        total = total / count
        print("mean of line",n,":",total)
        bob = bob + total
        total = 0
        count = 0
bob = bob / n
print("total mean :",bob)
file.close()
"""
"""
l = []
for line in file:
    if (len(line) > 1):
        num = line.strip() 
        num = num.split(",")
        l.extend(num)
l.sort()
if(len(l) % 2 == 0):
    median = (int(l[int(len(l)/2)])+int(l[int(len(l)/2+1)]))/2
else:
    median = l[int(len(l)//2+1)]
print(median)
file.close()
"""

numbers = {}
for num in file:
    num = num.strip()
    num = num.split(',')
    for number in num:
        if number in numbers:
            numbers[number] = numbers[number]+1
        else:
            numbers[number] = 1
print(numbers)
file.close()

"""
numbers = {}
for num in file:
    num = num.strip()
    num = num.split(',')
    for number in num:
        if number in numbers:
            numbers[number] = numbers[number]+1
        else:
            numbers[number] = 1
print(numbers)
file.close()
"""