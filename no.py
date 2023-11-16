runningTotal = 0
price1 = 10
runningTotal = runningTotal + price1
price2 = 14
runningTotal = runningTotal + price2
price3 = 6
runningTotal = runningTotal + price3

print(runningTotal)

file = open("myfile.txt")
print (file)
for line in file:
    print(line.strip())
file.close