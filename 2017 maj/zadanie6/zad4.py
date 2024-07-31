file = open("dane.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))


thebestdlugosc = 0

for x in range(0,320):
    aktualnadlugosc = 0
    aktualnaliczba = 0
    for y in range(0,200):
        sprawdzana = int(data[y][x])

        if(sprawdzana == aktualnaliczba):
            aktualnadlugosc+=1
        else:
            aktualnadlugosc=1
            aktualnaliczba = sprawdzana

        if(aktualnadlugosc > thebestdlugosc):
            thebestdlugosc = aktualnadlugosc
            print(thebestdlugosc,aktualnaliczba)

print(thebestdlugosc)



