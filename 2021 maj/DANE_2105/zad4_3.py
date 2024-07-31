import string

file = open('instrukcje.txt')

data = []

for l in file:
    data.append(l.strip().split(" "))

tab = string.ascii_uppercase
tab = list(tab)
tab2 = []
for i in tab:
    tab2.append(0)



for kom in data:
    if(kom[0] == "DOPISZ"):
        tab2[tab.index(kom[1])] +=1
print(tab[tab2.index(max(tab2))],max(tab2))


