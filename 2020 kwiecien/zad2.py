file = open("dane4.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

for index, i in enumerate(data):
    data[index] = int(i[0])

kontener = [[],[]]


aktualnawartosc = 0
indextabeli = 0

for index, i in enumerate(data):
    if(index+1 != len(data) and index!=0):

        wartosc = abs(data[index]-data[index+1])
        wartoscdotylu = abs(data[index-1] - data[index])


        print(i,wartosc,aktualnawartosc)
        if(wartosc == aktualnawartosc or wartoscdotylu == aktualnawartosc):
            kontener[indextabeli].append(i)

        if(wartosc != aktualnawartosc):
            kontener.append([])
            indextabeli+=1
            aktualnawartosc=wartosc
            kontener[indextabeli].append(i)

thebestciag = []
thebestdlugosc = 0

print(kontener)

for i in kontener:
    if(len(i) > thebestdlugosc):
        thebestdlugosc = len(i)
        thebestciag = i

print(thebestciag , thebestdlugosc)




