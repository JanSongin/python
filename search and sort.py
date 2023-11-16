#linear search
"""
lis = [15,4,41,13,24,14,12,21]
def linsearch(l):
    ask = int(input("Enter a number you want to search for "))
    i = 0
    while(len(l) > i):
        if(l[i] == ask):
            return i
        i = i + 1
    return -1
p = linsearch(lis)
print(p)
"""
#binary search

lis = [15,4,41,13,24,14,12,21]
def binsearch(l):
    l.sort()
    ask = int(input("Enter a number you want to search for "))
    i = 0
    high = len(l)
    mid = high