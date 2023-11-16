#card = 8549018035096133
card = int(input("Enter your card number: "))
card = str(card)
count = 0
listcard = []
while (len(card) > count):
    listcard.append(card[count])
    listcard[count] = int(listcard[count])
    count = count + 1
lastdigit = listcard.pop(-1)
listcard.reverse()
sumcard = listcard[1::2]
sumcardtimes2 = listcard[0::2]
count = 0
while(len(sumcardtimes2) > count):
    sumcardtimes2[count] = sumcardtimes2[count] * 2
    if(sumcardtimes2[count] > 9):
        sumcardtimes2[count] = sumcardtimes2[count] - 9
    count = count + 1
sumcard = sum(sumcard) + sum(sumcardtimes2) + lastdigit
sumcard = sumcard % 10
if (sumcard == 0):
    print("Your card is valid")
else:
    print("Your card is invalid")