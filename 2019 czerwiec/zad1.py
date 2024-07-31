file = open("liczby.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

print(data)

for index, i in enumerate(data):
    data[index] = int(i[0])

print(data)

def czypierwsza(liczba):
    if(liczba == 1):
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True



for i in data:
    if(i>=100 and i<=5000 and czypierwsza(i)):
        print(i)