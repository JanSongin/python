#20
#name = input("Enter your name ")
#length = len(name)
#print("Your name is",length,"characters long")

#21
#name2 = input("Enter your name ")
#surname = input("Enter your surname ")
#fullname = name2 + " " + surname
#print(fullname)

#22
#name3 = input("Enter your first name and surname in lower case ")
#nameupper = name3.upper()
#print(nameupper)

#23
#rhyme = input("Enter a rhyme ")
#length2 = len(rhyme)
#print(length2)
#n1 = int(input("Where to start from ")) - 1
#n2 = int(input("Where to end "))
#rhyme = rhyme[n1:n2]
#print(rhyme)

#24
#word = input("Enter a word ")
#up = word.upper()
#print(up)

#25
#name4 = input("Enter your name ")
#length3 = len(name4)
#if (length3 < 5):
#    surname2 = input("Enter your surname ")
#    name4 = name4.upper()
#    fullname2 = name4 + surname2
#    print(fullname2)
#else:
#    print(name4)

#26
word2 = input("Enter a word ")
word2 = word2.lower()
if (word2[0] == "a"):
    print(word2 + "way")
elif (word2[0] == "e"):
    print(word2 + "way")
elif (word2[0] == "i"):
    print(word2 + "way")
elif (word2[0] == "o"):
    print(word2 + "way")
elif (word2[0] == "u"):
    print(word2 + "way")
else:
    print("ay" + word2)
    