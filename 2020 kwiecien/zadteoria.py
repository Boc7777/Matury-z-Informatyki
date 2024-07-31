n = 10
T = [4,4,1,4,1,4,7,4,9,2]

max = 0

for i in range(0,n):
    if(T[i] > max):
        max = T[i]


thebestilosc = 0
thebestmoda = 0

for liczba in range(0,max+1):
    aktualnailosc = 0

    for i in range(0,n):
        if(T[i] == liczba):
            aktualnailosc +=1


    if(aktualnailosc>thebestilosc):
        thebestilosc = aktualnailosc
        thebestmoda = liczba

print(thebestmoda)






