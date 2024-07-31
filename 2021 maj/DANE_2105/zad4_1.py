file = open('instrukcje.txt')

data = []

for l in file:
    data.append(l.strip().split(" "))

ilosc = 0
for kom in data:
    if(kom[0] == "DOPISZ"):
        ilosc +=1
    elif(kom[0] =="USUN"):
        ilosc -=1

print(ilosc)