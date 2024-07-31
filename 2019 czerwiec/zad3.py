file = open("pierwsze.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

for index, i in enumerate(data):
    data[index] = i[0]



def waga(liczba):
    suma = 0
    for i in range(0,len(liczba)):
        suma += int(liczba[i])
    return suma


iloscjedynkowych = 0
for i in data:
    trzymak = waga(i)
    while(trzymak>9):
        trzymak = waga(str(trzymak))

    if(trzymak == 1):
        iloscjedynkowych+=1

print(iloscjedynkowych)
