
tab = ['A', 'B', 'C', 'A', 'A', 'B', 'B', 'D']


obiekt = {}

for i in tab:
    if i in obiekt:
        obiekt[i]+=1
    else:
        obiekt[i] = 1


maks = max(obiekt.values())


for i in obiekt:
    if obiekt[i] == maks:
        print(i)



