file = open('Dane_2103/galerie.txt')
data = []
for l in file:
    data.append(l.strip().split(' '))


def czyjest(tab,liczba):
    for i in tab:
        if(i == liczba):
            return False
    return True

najmnieszemiasto = ""
najmnieszeindex =99

najwieszemiasto =""
najwiekszyindex =0
for miasta in data:

    tabpowierzchnia = []

    for i in range(2, len(miasta),2):
        powierzchnia = int(miasta[i]) * int(miasta[i + 1])
        if(czyjest(tabpowierzchnia,powierzchnia) and powierzchnia!=0):
            tabpowierzchnia.append(powierzchnia)

    if(len(tabpowierzchnia)>najwiekszyindex):
        najwiekszyindex = len(tabpowierzchnia)
        najwieszemiasto = miasta[1]

    if (len(tabpowierzchnia) < najmnieszeindex):
        najmnieszeindex = len(tabpowierzchnia)
        najmnieszemiasto = miasta[1]

print(najwieszemiasto, najwiekszyindex)
print(najmnieszemiasto, najmnieszeindex)







