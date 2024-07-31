file = open("identyfikator.txt","r")
data = []
for l in file:
    data.append(l.strip())



for i in data:
    czypolidrom = False
    seria = i[0:3]
    cyfry = i[3:]

    if(seria[0] == seria[2]):
        czypolidrom = True

    if(cyfry[0] == cyfry[5] and cyfry[1] == cyfry[4] and cyfry[2] == cyfry[3]):
        czypolidrom = True

    if(czypolidrom):
        print(i)

