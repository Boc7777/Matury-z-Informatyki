file = open('Dane_2103/galerie.txt')
data = []
for l in file:
    data.append(l.strip().split(' '))

tablicaKodow = []

for kod in data:
    tablicaKodow.append(kod[0])




tablicaKodow = list(set(tablicaKodow))

tablicailosci = []
for i in tablicaKodow:
    tablicailosci.append(0)


print(tablicaKodow)

for kod in data:
    tablicailosci[tablicaKodow.index(kod[0])] +=1

# print(tablicaKodow)
# print(tablicailosci)

for index, i in enumerate(tablicaKodow):
    print(tablicaKodow[index]," ",tablicailosci[index])
