file = open("napisy.txt","r")
data = []
for l in file:
    data.append(list(l.strip()))

napis = ""

for zestaw in data:
    cyfrytab = []
    for a in zestaw:

        if(a=="0"or a=="1"or a=="2"or a=="3"or a=="4"or a=="5"or a=="6"or a=="7"or a=="8"or a=="9"):
            cyfrytab.append(a)
    if(len(cyfrytab)%2!=0):
        cyfrytab.pop()

    # print(cyfrytab)

    cyfrytab2 = []

    for i in range(0,int(len(cyfrytab))):
        if(i%2==0):
            liczba = int(cyfrytab[i] + cyfrytab[i+1])
            cyfrytab2.append(liczba)

    # print(cyfrytab2)

    for i in cyfrytab2:
        if(i >=65 and i<=90):
            napis+=chr(i)

print(napis)


