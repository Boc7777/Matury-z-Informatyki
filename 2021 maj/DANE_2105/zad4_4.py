import string

file = open('instrukcje.txt')

data = []

for l in file:
    data.append(l.strip().split(" "))

napis = []

tab = string.ascii_uppercase
tab = list(tab)

for kom in data:
    if(kom[0] == "DOPISZ"):
        napis.append(kom[1])
    if (kom[0] == "USUN"):
        napis.pop()
    if (kom[0] == "ZMIEN"):
        napis[-1] = kom[1]
    if (kom[0] == "PRZESUN"):
        for index, literka in enumerate(napis):
            if(kom[1] == literka):
                if(kom[1] == "Z"):
                    napis[index] = 'A'
                else:
                    napis[index] = tab[tab.index(kom[1])+1]
                break

print(''.join(napis))


siema = "sdasad"

print(siema[:-1]+"s")

