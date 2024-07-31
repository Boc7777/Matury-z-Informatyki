file = open("dane.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

licznik = 0
for y in range(0,200):
    for x in range(0,320):
        prawy = True
        lewy = True
        gorny = True
        dolny = True

        if(x-1<0):
            lewy = False
        if (x + 1 > 319):
            prawy = False
        if(y-1<0):
            gorny = False
        if(y+1>199):
            dolny = False


        wartosc = int(data[y][x])
        czykontrast = False

        if(lewy):
            sasiad = int(data[y][x-1])
            if(abs(wartosc-sasiad) >128):
                czykontrast = True
                print(y,x,"lewy")


        if (prawy):
            sasiad = int(data[y][x + 1])
            if (abs(wartosc - sasiad) > 128):
                czykontrast = True
                print(y, x ,"prawy")


        if (gorny):
            sasiad = int(data[y-1][x])
            if (abs(wartosc - sasiad) > 128):
                czykontrast = True
                print(y, x,"gorny")


        if (dolny):
            sasiad = int(data[y+1][x])
            if (abs(wartosc - sasiad) > 128):
                czykontrast = True
                print(y,x,"dolny")

        if(czykontrast):
            licznik+=1

print(licznik)










