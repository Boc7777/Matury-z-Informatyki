file1 = open("dane1.txt","r")

data1 = []
for l in file1:
    data1.append(l.strip().split(" "))



file2 = open("dane2.txt","r")

data2 = []
for l in file2:
    data2.append(l.strip().split(" "))

file3 = open("JD.txt","w")


for i in range(0,len(data1)):
    index1 = 0
    index2 = 0
    tab = []
    while (index1+index2) <20:

        if(index1!=10 and index2!= 10):
            if(int(data1[i][index1]) <= int(data2[i][index2])):
                tab.append(data1[i][index1])
                index1 += 1
            else:
                tab.append(data2[i][index2])
                index2 += 1
        else:
            if(index1 == 10):
                for cyfra in range(index2,10):
                    tab.append(data2[i][cyfra])
                    index2 += 1

            if(index2 == 10):
                for cyfra in range(index1,10):
                    tab.append(data1[i][cyfra])
                    index1 += 1





    for i in tab:
        file3.write(str(i)+" ")
    file3.write("\n")














