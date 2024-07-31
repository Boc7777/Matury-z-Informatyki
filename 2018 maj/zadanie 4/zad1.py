file = open("sygnaly.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))


slowo = ""
for index,i in enumerate(data):
    if(index !=0 and (index+1)%40 == 0 ):
        slowo += data[index][0][9]

print(slowo)