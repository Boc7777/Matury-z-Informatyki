file = open("./Dane_2212/liczby.txt")
data = []
for l in file:
    data.append(l.strip())

for index, i in enumerate(data):
    data[index] = int(i)

# print(data)


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



tab = Eratostenes(1000000)

suma = 0
for i in data:
    if(tab[i-1] == True):
        suma+=1

print(suma)