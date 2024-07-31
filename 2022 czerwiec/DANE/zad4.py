file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

print(data)

for index, i in enumerate(data):
    data[index] = int(i[0])

print(len(list(set(data))))

databezpowtorek = list(set(data))

licznikdwujakwo = 0

for i in databezpowtorek:
    liczniklokalny = 0
    for a in data:
        if(a == i):
            liczniklokalny+=1
    if(liczniklokalny == 2):
        licznikdwujakwo +=1

print(licznikdwujakwo)

liczniktrojakow = 0

for i in databezpowtorek:
    liczniklokalny = 0
    for a in data:
        if(a == i):
            liczniklokalny+=1
    if(liczniklokalny == 3):
        liczniktrojakow +=1

print(liczniktrojakow)



