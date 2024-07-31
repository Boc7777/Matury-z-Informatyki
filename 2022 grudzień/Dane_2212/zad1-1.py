file = open("mecz.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

data = list(data[0][0])

licznik = 0
for i in range(1,len(data)):
    if(data[i]!= data[i-1]):
        licznik+=1
print(licznik)

