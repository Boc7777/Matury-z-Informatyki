file = open("anagram.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))


tab = []
for i in data:
    tab.append(str(int(i[0],2)))

bezzerowych = 0
for i in tab:
    liczba = i
    tab2 = list(liczba)
    czyznalezionozero = False
    for a in tab2:
        if(int(a) == 0 ):
            czyznalezionozero= True

    if(czyznalezionozero == False):
        bezzerowych+=1

print(bezzerowych)


thebestliczba = ""
thebestsuma = 0

for i in tab:
    liczba = i
    tab2 = list(set(list(liczba)))
    suma = 0
    for a in tab2:
        suma+=int(a)
    if(suma>thebestsuma):
        thebestsuma = suma
        thebestliczba = i

print(thebestliczba)


