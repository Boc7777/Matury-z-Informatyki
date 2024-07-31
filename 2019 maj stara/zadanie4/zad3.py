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

tabwielkosci = []

for index, dzialka in enumerate(gigatab):
    znalezionepole = False

    glebokosc_wiersza = 30
    iloscwzietychwierszy = 30

    while(znalezionepole==False):
        znalezionepole=True


        for index_wiersz in range(0,iloscwzietychwierszy):
            for index_pole in range(0,glebokosc_wiersza):
                if(dzialka[index_wiersz][0][index_pole] == "X"):

                    glebokosc_wiersza-=1
                    iloscwzietychwierszy-=1
                    znalezionepole = False
                    break



    tabwielkosci.append(glebokosc_wiersza)

maks = max(tabwielkosci)

for index,i in enumerate(tabwielkosci):
    if(i==maks):
        print(index+1,i)



