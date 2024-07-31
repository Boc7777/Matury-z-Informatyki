file = open("anagram.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))

zrownowazone = 0
prawiezrownowazone = 0

for i in data:
    liczba = i[0]
    tab = list(liczba)
    ilosczer = 0
    iloscjedynek = 0
    for cyfra in tab:
        if(int(cyfra) == 1 ):
            iloscjedynek +=1
        else:
            ilosczer+=1

    if(ilosczer== iloscjedynek):
        zrownowazone+=1
    elif(abs(ilosczer-iloscjedynek)==1):
        prawiezrownowazone+=1

print(zrownowazone,prawiezrownowazone)

