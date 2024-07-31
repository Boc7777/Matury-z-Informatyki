file = open("mecz.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

data = list(data[0][0])

thebestdruzyna = ""
thebestpassa = 0
ilsocpasswszystkich = 0

aktualnadruzyna = ""
aktualnylicznik = 0
for i in data:
    if(aktualnadruzyna == i):
        aktualnylicznik+=1
    else:
        aktualnadruzyna = i
        aktualnylicznik=1


    if(aktualnylicznik == 10):
        ilsocpasswszystkich +=1

    if(aktualnylicznik>thebestpassa):
        thebestpassa= aktualnylicznik
        thebestdruzyna = aktualnadruzyna

print(ilsocpasswszystkich,thebestdruzyna,thebestpassa)






