file = open("mecz.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

data = list(data[0][0])


licznikA = 0
licznikB = 0

for i in data:
    if i == "A":
        licznikA+=1
    else:
        licznikB+=1
    if(licznikA >=1000 or licznikB >= 1000):
        if(abs(licznikA-licznikB) >= 3):
            print(licznikA,licznikB)
            break