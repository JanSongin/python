#0
runningTotal = 0
price1 = 12
runningTotal = runningTotal + price1
price2 = 24
runningTotal = runningTotal + price2
price3 = 36
runningTotal = runningTotal + price3
price4 = 48
runningTotal = runningTotal + price4

print(runningTotal)

#1
#file = open("daffodils.txt")
#for line in file:
#    print(line.strip())
#file.close

#2
#file = open("daffodils.txt")
#count = 0
#for line in file:
#    print(line)
#    count += 1
#print(count)
#file.close

#3
#file = open("num_calc_1.txt")
#number = 0
#count = 0
#for line in file:
#    line = line.strip()
#    if(line.isdigit()):
#        number = number + int(line)
#        count += 1
#mean = number / count
#print(mean)
#file.close

#4
#l = 20
#mean = 0
#personsay = 0
#while(l > 0):
#    personsay = int(input("Give 20 numbers "))
#    l = l - 1
#    mean = mean + personsay
#mean = mean / 20
#print("The mean is ",mean)

#5
file = open("mean.txt","w")
l = 10
number = 0
count = 0
while(l > 0):
    personsay = input("Give 10 numbers ")
    l = l - 1
    file.write(personsay + "\n")
file.close()
file = open("mean.txt")
for line in file:
    line = line.strip()
    if(line.isdigit()):
        number = number + int(line)
        count += 1
mean = number / count
print(mean)
file.close()