file = open("punkty.txt","r")
data = []
for l in file:
    data.append(l.strip().split())

for index,i in enumerate(data):
    tab = [int(data[index][0]) ,int(data[index][1])]
    data[index] = tab

srodkowe = 0
wewnetrzne = 0
zewnetrzne = 0
for punkt in data:

    if((punkt[0] == 5000 and punkt[1]<=5000 )or (punkt[1] == 5000  and punkt[0] <=5000) ):
        srodkowe+=1
    elif(punkt[0]<5000 and punkt[1]<5000):
        wewnetrzne+=1
    elif(punkt[0]>5000 or punkt[1]>5000):
        zewnetrzne+=1


print(srodkowe,wewnetrzne,zewnetrzne)
print(len(data))