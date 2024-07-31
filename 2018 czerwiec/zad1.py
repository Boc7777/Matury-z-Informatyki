file1 = open("dane1.txt","r")

data1 = []
for l in file1:
    data1.append(l.strip().split(" "))



file2 = open("dane2.txt","r")

data2 = []
for l in file2:
    data2.append(l.strip().split(" "))


print(data1)
print(data2)
licznik = 0
for i in range(0,len(data1)):
    if(data1[i][-1] == data2[i][-1]):
        licznik+=1
print(licznik)


