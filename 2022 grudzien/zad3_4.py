file = open("./Dane_2212/liczby.txt")
data = []
for l in file:
    data.append(l.strip())

for index, i in enumerate(data):
    data[index] = int(i)

tab1 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
tab2 = []

for i in tab1:
    tab2.append(0)

for liczba in data:

    w16 = str(hex(liczba))[2:]
    tab = list(w16)
    for i in tab:
        tab2[tab1.index(i)]+=1


for index, i in enumerate(tab1):
    print(i,":",tab2[index])





