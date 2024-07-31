file = open("pary.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

for i in data:
    i[0] = int(i[0])
    i[1] = int(i[1])


for zestaw in data:
    zakres = 2
    poczatkowa = zestaw[0]
    granica = zestaw[1]

    while poczatkowa*2<granica:
        poczatkowa= poczatkowa*2
        zakres = zakres*2
        # print(poczatkowa,zakres)

    # print(zestaw[0],poczatkowa,granica)
    if(abs(poczatkowa-granica)<=zakres):
        print(zestaw[0],granica)
