#1
#P1
#abcdefghijklmnopqrstuvwxyz
#DEFGHIJKLMNOPQRSTUVWXYZABC

#P2
#Athlone Community College
#DWKORQH FRPPXQLWB FROOHJH

#P3
#25

#P4
#what do you get when you
#ZKDW GR BRX JHW ZKHQ BRX
#cross a snowman with a
#FURVV D VQRZPDQ ZLWK D
#vampire? frostbite
#YDPSLUH? IURVWELWH

#2
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
cipher = input("Enter your cipher ")
encode = input("Do you want to encode or decode ")
key = int(input("Enter the key "))

for alphabet in range (0,25,1):
    print(alphabet[alphabet.index(cipher) + key])