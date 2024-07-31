file = open("./Dane_2212/mecz.txt")
data = []
for l in file:
    data.append(l.strip())

data = data[0]

suma = 0
for index, mecz in enumerate(data):
    if(index!= 0):
        if(data[index]!= data[index-1]):
            suma+=1
print(suma)

