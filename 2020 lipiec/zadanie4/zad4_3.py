import string

file = open("identyfikator.txt","r")
data = []
for l in file:
    data.append(l.strip())

alf = list(string.ascii_uppercase)


for i in data:
    seria = i[0:3]
    kontrol = i[3]
    cyfry = i[4:]
    suma = 0

    suma+= (((alf.index(seria[0])+10)*7) +
             ((alf.index(seria[1])+10)*3) +
             ((alf.index(seria[2])+10)*1))

    suma+= ((int(cyfry[0])*7)+
            (int(cyfry[1])*3)+
            (int(cyfry[2])*1)+
            (int(cyfry[3])*7)+
            (int(cyfry[4])*3))

    if(suma %10 != int(kontrol)):
        print(i)
