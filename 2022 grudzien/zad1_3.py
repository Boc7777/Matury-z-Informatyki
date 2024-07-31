file = open("./Dane_2212/mecz.txt")
data = []
for l in file:
    data.append(l.strip())

data = data[0]

aktualny_licznik = 0
aktualnadruzyna = ""

passyA = 0
passyB = 0

thebestdruzyna = ""
thebestdlugosc = 0

for mecz in data:
    if(mecz != aktualnadruzyna):
        aktualnadruzyna = mecz
        aktualny_licznik=1
    else:
        aktualny_licznik+=1

    if(aktualny_licznik==10):
        if(aktualnadruzyna == "A"):
            passyA+=1
        else:
            passyB+=1

    if(aktualny_licznik>thebestdlugosc):
        thebestdlugosc = aktualny_licznik
        thebestdruzyna = aktualnadruzyna


print(passyA+passyB,thebestdruzyna,thebestdlugosc)