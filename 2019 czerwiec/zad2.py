file = open("pierwsze.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

for index, i in enumerate(data):
    data[index] = i[0]


def czypierwsza(liczba):
    if(liczba == 1):
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True



for i in data:
    pierwotna = int(i)
    odwrocona = int(i[::-1])
    if(czypierwsza(pierwotna) and czypierwsza(odwrocona)):
        print(pierwotna)