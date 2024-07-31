file = open("dzialki.txt","r")
data = []
for i in file:
    data.append(i.strip().split(" "))


gigatab=[]
minitab = []
for i in data:
    if(len(i[0])>0):
        minitab.append(i)
    else:
        gigatab.append(minitab)
        minitab = []



gigatabodwrotna = []
for dzialka in gigatab:
    minitab = []
    for wiersz in reversed(dzialka):
        wiersz = [wiersz[0][::-1]]
        minitab.append(wiersz)
    gigatabodwrotna.append(minitab)



wyniktab = []

for indexOD,odwrocona  in enumerate(gigatabodwrotna):
    for indexNO,normalna in enumerate(gigatab):
        if(odwrocona == normalna):
            wyniktab.append([indexOD+1,indexNO+1])

print(wyniktab)

for i in wyniktab:
    for index, a in enumerate(wyniktab):
        print(i[0],i[1],a[0],a[1])
        if(i[0] == a[1]):
            wyniktab[index] = [0,0]

print(wyniktab)

for i in wyniktab:
    if(i[0]==0 and i[1]==0):
        pass
    else:
        print(i[0],i[1])




