file = open("identyfikator.txt","r")
data = []
for l in file:
    data.append(l.strip())

thebestident = ""
thebestwielkosc = 0

for i in data:
    numerki = i[3:]
    tab = list(numerki)
    suma = 0
    for cyfra in tab:
        suma += int(cyfra)
    if(suma > thebestwielkosc):
        thebestwielkosc = suma
        thebestident = i

print(thebestident)


