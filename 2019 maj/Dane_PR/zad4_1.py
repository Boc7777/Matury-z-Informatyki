file = open("liczby.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

for index,i in enumerate(data):
    data[index] = int(i[0])


liczenie = 0
for i in data:
    poczatkowa = 3
    liczba = 1
    while liczba <=100000 and liczba<=i:

        if(i == liczba):
            liczenie+=1
            print(i, liczba)
            break
        liczba = liczba * poczatkowa

print(liczenie)