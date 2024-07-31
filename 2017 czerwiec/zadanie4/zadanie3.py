file = open("punkty.txt","r")
data = []
for l in file:
    data.append(l.strip().split())

for index,i in enumerate(data):
    tab = [int(data[index][0]) ,int(data[index][1])]
    data[index] = tab


thebestodleglosc = 0
thebestpunkt1 = [0,0]
thebestpunkt2 = [0,0]

for punkt1 in data:
    for punkt2 in data:
       odleglosc =  ( ((punkt2[0] - punkt1[0])**2) + ((punkt2[1] - punkt1[1] ) **2)   )**0.5

       if(odleglosc>thebestodleglosc):
            thebestodleglosc = odleglosc
            thebestpunkt1 = punkt1
            thebestpunkt2 = punkt2

print(round(thebestodleglosc),thebestpunkt1,thebestpunkt2)
