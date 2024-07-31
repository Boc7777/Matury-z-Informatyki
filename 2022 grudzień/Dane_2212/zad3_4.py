file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))


for index, i in enumerate(data):
    data[index] = int(i[0])


tab1 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
tab2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for i in data:
    szesta = str(hex(i))
    szesta = list(szesta)
    szesta = szesta[2:]
    for a in szesta:
        tab2[tab1.index(a)]+=1

for i in range(0,len(tab1)):
    print(tab1[i],":",tab2[i])