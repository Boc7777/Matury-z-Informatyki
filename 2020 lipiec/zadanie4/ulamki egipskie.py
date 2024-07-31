import math

p = 4
q = 5

def NWW(x,y):
    pierwsza = x
    druga = y
    while pierwsza!=druga:
        if(pierwsza>druga):
            druga = druga + y
        else:
            pierwsza = pierwsza + x
    return pierwsza

def rozklad(p,q):

    ulamek =  p/q
    odwrotnosc = q/p

    n = math.floor(odwrotnosc)
    if(odwrotnosc%1!=0):
        n+=1
    print(n)
    wspolny = NWW(q,n)
    mnoznik1 = wspolny/q
    mnoznik2 = wspolny/n
    licznik1 = p*mnoznik1
    licznik2 = mnoznik2

    licznikR = licznik1-licznik2
    if(licznikR!=0):
        rozklad(int(licznikR),wspolny)






rozklad(p,q)