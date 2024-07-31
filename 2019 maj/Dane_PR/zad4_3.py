file = open("liczby.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

for index,i in enumerate(data):
    data[index] = int(i[0])


def NWD(liczb1,liczb2):
    tab1 = []
    dzielnik1 = 2
    while liczb1 != 1:
        if(liczb1%dzielnik1==0):
            tab1.append(dzielnik1)
            liczb1=liczb1/dzielnik1
        else:
            dzielnik1+=1

    tab2 = []
    dzielnik2 = 2
    while liczb2 != 1:
        if (liczb2 % dzielnik2 == 0):
            tab2.append(dzielnik2)
            liczb2 = liczb2 / dzielnik2
        else:
            dzielnik2 += 1


    tab3 = []
    for i in tab1:
        if i in tab2:
            tab3.append(i)
            tab2[tab2.index(i)] = 0

    wynik = 1
    for i in tab3:
        wynik = wynik * i
    return wynik



thebestpierwsza = 0
thebestdzielnik = 0
thebestdlugosc = 0

for index,i in enumerate(data):
    if(index+1 != len(data)):
        pierwsza = data[index]
        dzielnik = NWD(data[index],data[index+1])
        dlugosc = 2

        if(dzielnik>1):
            for index2 in range(index+2,len(data)):
                if(NWD(dzielnik,data[index2]) == dzielnik):
                    dlugosc+=1
                else:
                    break

                if(dlugosc>thebestdlugosc):
                    thebestpierwsza = pierwsza
                    thebestdzielnik = dzielnik
                    thebestdlugosc = dlugosc


print(thebestpierwsza,thebestdlugosc,thebestdzielnik)









