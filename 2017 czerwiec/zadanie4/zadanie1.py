file = open("punkty.txt","r")
data = []
for l in file:
    data.append(l.strip().split())

for index,i in enumerate(data):
    tab = [int(data[index][0]) ,int(data[index][1])]
    data[index] = tab


def czypierwsza(a):
    if(a == 1):
        return False
    for i in range(2,a):
        if(a%i == 0):
            return False
    return True


suma = 0

for i in data:
    if(czypierwsza(i[0]) and czypierwsza(i[1])):
        suma+=1
        print(i)
print(suma)





