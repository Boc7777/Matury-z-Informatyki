file = open("liczby.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

for index,i in enumerate(data):
    data[index] = int(i[0])



def liczniesilni(cyfra):
    if(cyfra==0):
        return 1
    else:
        mnoznik = 1
        for i in range(1,cyfra+1):
            mnoznik = mnoznik * i
        return  mnoznik




for i in data:
    startowa = i
    domodyfikacji = list(str(i))
    suma = 0
    for cyfra in domodyfikacji:
        suma += liczniesilni(int(cyfra))

    if(suma == startowa):
        print(startowa)

