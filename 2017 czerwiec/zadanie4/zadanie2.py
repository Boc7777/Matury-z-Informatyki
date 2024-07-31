file = open("punkty.txt","r")
data = []
for l in file:
    data.append(l.strip().split())


suma = 0

for i in data:
    tab1 = list(set(list(i[0])))

    tab2 = list(set(list(i[1])))
    czygit = True
    for i in tab1:
        if i not in tab2:
            czygit = False

    for i in tab2:
        if i not in tab1:
            czygit = False

    if(czygit):
        suma+=1
        print(i,tab1,tab2)

print(suma)



