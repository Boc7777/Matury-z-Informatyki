file = open("dane4.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

for index, i in enumerate(data):
    data[index] = int(i[0])


tabluk  = []
tabwartosci = []


for index, i in enumerate(data):
    if (index != 0):
        luka = abs(data[index - 1] - data[index])
        if luka in tabluk:
            tabwartosci[tabluk.index(luka)]+=1
        else:
            tabluk.append(luka)
            tabwartosci.append(1)

print(tabluk)
print(tabwartosci)

for index,i in enumerate(tabwartosci):
    if(i>5):
        print(i,tabluk[index])