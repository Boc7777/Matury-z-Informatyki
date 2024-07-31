file1 = open("dane1.txt","r")

data1 = []
for l in file1:
    data1.append(l.strip().split(" "))



file2 = open("dane2.txt","r")

data2 = []
for l in file2:
    data2.append(l.strip().split(" "))

tab = []
ilosc = 0
for i in range(0,len(data1)):
    czygit = True
    for cyfra in range(0,10):

        if data1[i][cyfra] not in data2[i]:
            czygit= False

        if data2[i][cyfra] not in data1[i]:
            czygit = False
    if(czygit):
        tab.append(i+1)
        ilosc+=1
print(ilosc)
print(tab)





