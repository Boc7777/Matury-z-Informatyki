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

iloscdzialek70 = 0
for dzialka in gigatab:
    ilosctrawy = 0
    for wiersz in dzialka:
        for pole in wiersz[0]:
            if(pole == "*"):
                ilosctrawy+=1

    print(ilosctrawy , ilosctrawy/900)
    if(ilosctrawy/900 >=0.70):
        iloscdzialek70+=1
print(iloscdzialek70)


