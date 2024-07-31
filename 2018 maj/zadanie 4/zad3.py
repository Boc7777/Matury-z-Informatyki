file = open("sygnaly.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))


alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in data:
    slowo = i[0]
    tab = list(slowo)
    czygit = True
    for literka1 in tab:
        index1 = alf.index(literka1)
        for literka2 in tab:
            index2 = alf.index(literka2)
            odleglosc = abs(index1-index2)
            if(odleglosc>10):
                czygit=False
    if(czygit):
        print(slowo)




