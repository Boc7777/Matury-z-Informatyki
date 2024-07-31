file = open("./Dane_2212/liczby.txt")
data = []
for l in file:
    data.append(l.strip())

for index, i in enumerate(data):
    data[index] = int(i)

def Eratostenes(N):
    tab = []
    for i in range(0,N+1):
        tab.append(True)
    tab[0] = 0
    tab[1] = False

    for index, i in enumerate(tab):
        if(index>=2):
            if(i == True):
                j=index+index
                while j<=N:
                    tab[j] = False
                    j=j+index

    return tab



pierwsze = Eratostenes(1000000)


thebestilosc = 0
thebestliczba = 0

theworstilosc = 9999999999999999
theworstliczba = 0


for i in data:
    if(i%2==0):
        ilosc = 0
        for liczba1 in range(2,i):
            liczba2 = i-liczba1
            if(pierwsze[liczba1] == True and pierwsze[liczba2]==True):
                ilosc+=1


    if(ilosc>thebestilosc):
        thebestilosc = ilosc
        thebestliczba = i
    if(ilosc<theworstilosc):
        theworstilosc = ilosc
        theworstliczba = i

print(thebestliczba,int(thebestilosc/2))

print(theworstliczba,int(theworstilosc/2))
