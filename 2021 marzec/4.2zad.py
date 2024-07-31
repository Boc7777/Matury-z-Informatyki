file = open('Dane_2103/galerie.txt')
data = []
for l in file:
    data.append(l.strip().split(' '))

tab = []
for miasta in data:

    powierzchnia = 0
    liczbalokali = 0

    for i in range(2, len(miasta),2):
        powierzchnia += int(miasta[i])*int(miasta[i+1])
        if(int(miasta[i])*int(miasta[i+1]) != 0):
            liczbalokali +=1

    tab.append([miasta[1],powierzchnia,liczbalokali])
print(tab)

najwiekszy = tab[0]
najmnieszy = tab[0]

for zestaw in tab:
    if(zestaw[1]>najwiekszy[1]):
        najwiekszy = zestaw

    if (zestaw[1] < najmnieszy[1]):
        najmnieszy = zestaw

print(najwiekszy)
print(najmnieszy)



