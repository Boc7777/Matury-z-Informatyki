file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))


for index, i in enumerate(data):
    data[index] = int(i[0])


def tablicaPierwszych(liczba):
    tab = []
    for i in range(0,liczba+1):
        tab.append(True)
    tab[0] = False
    tab[1] = False

    for i in range(1,liczba+1):
        if(tab[i] == True):
            j = i*2
            while j <= len(tab)-1:
                tab[j] = False
                j= j+i
    return tab


pierwsze = tablicaPierwszych(1000001)

licznik = 0
for i in data:
    if(pierwsze[i-1] == True):
        licznik+=1

print(licznik)



