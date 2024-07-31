file = open("sygnaly.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))


thebestilosc = 0
thebestslowo = ""

for i in data:
    slowo = i[0]
    tab = list(slowo)
    tab2 = list(set(tab))
    if(len(tab2) > thebestilosc):
        thebestilosc = len(tab2)
        thebestslowo = slowo

print(thebestslowo, thebestilosc)