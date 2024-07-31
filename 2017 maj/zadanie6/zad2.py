file = open("dane.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))


niegit = 0
for index, i in enumerate(data):
    czygitwiersz = True
    for i in range(0,160):
        # print(i,320-i-1)
        if(data[index][i] != data[index][319-i]):
            czygitwiersz = False
            break
    if(czygitwiersz == False):
        niegit +=1

print(niegit)
