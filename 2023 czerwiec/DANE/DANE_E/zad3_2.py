import math

file = open("anagram.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))

megatab = []

for i in data:
    if(len(i[0]) == 8):
        dlugosc = len(i[0])-1
        tab2 = list(i[0])
        ilosczer = 0
        iloscjedynek = -1

        for a in tab2:
            if(int(a) == 1):
                iloscjedynek+=1
            else:
                ilosczer+=1

        mozliwosci = math.factorial(dlugosc)/(math.factorial(iloscjedynek) * math.factorial(dlugosc-iloscjedynek))
        megatab.append([i,mozliwosci])

najwieksza = 0
for i in megatab:
    if(i[1] > najwieksza):
        najwieksza = i[1]

for i in megatab:
    if(i[1] == najwieksza):
        print(i)


