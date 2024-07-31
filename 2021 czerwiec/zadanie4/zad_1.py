file = open("napisy.txt","r")
data = []
for l in file:
    data.append(list(l.strip()))

suma = 0
for i in data:
    for a in i:
        if(a=="0"or a=="1"or a=="2"or a=="3"or a=="4"or a=="5"or a=="6"or a=="7"or a=="8"or a=="9"):
            suma+=1
print(suma)