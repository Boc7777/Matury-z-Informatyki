file = open("./Dane_2212/pary.txt")
data = []
for l in file:
    data.append(l.strip().split(" "))

for index,i in enumerate(data):
    data[index][0] = int(data[index][0])
    data[index][1] = int(data[index][1])

def rysuj(x,n):

    if(x<=n):
        tab1 = rysuj(2*x,n)
        tab2 = rysuj(2*x+1,n)

        tab3 = [2*x,2*x+1,x]

        maintab = tab3+tab1+tab2

        return maintab

    else:
        return []


for i in data:
    tab = rysuj(i[0], i[1])

    if(i[1] in tab):
        print(i[0],i[1])

