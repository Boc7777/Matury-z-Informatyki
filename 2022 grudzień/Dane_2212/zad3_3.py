file = open("siema","r")
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

tablicatylkopierwszych  = []

for index, i in enumerate(pierwsze):
    if i == True:
        tablicatylkopierwszych.append(index)

print(tablicatylkopierwszych)

thebestliczba = 0
thebestilosc = 0
najmniejszaliczba = 0
najmniejszailoscliczba = 99999999

for liczba in data:
    if(liczba>2 and liczba%2==0):
        licznik = 0
        for pierwsza in range(2,liczba):
            if(pierwsze[pierwsza] == True):
                for druga in range(pierwsza,liczba):
                    if(pierwsze[druga] == True):
                        if(pierwsza + druga == liczba):
                            licznik+=1





        if(licznik>thebestilosc):
            thebestliczba = liczba
            thebestilosc = licznik
        if(licznik<najmniejszailoscliczba):
            najmniejszaliczba = liczba
            najmniejszailoscliczba= licznik


print(thebestliczba,thebestilosc)
print(najmniejszaliczba,najmniejszailoscliczba)



