file = open("dane4.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

for index, i in enumerate(data):
    data[index] = int(i[0])


najwiekszy = 0
najmniejszy = 999999


for index, i in enumerate(data):
    if(index != len(data)-1):
        wartosc = abs(data[index]-data[index+1])

        if(wartosc>najwiekszy):
            najwiekszy = wartosc
        if(wartosc<najmniejszy):
            najmniejszy = wartosc

print(najwiekszy,najmniejszy)

