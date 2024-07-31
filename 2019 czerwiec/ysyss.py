import string

file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))



oniekt = {'Budapeszt': {'Pole': 3598, 'Lokale': 64}, 'Neapol': {'Pole': 3352, 'Lokale': 48}, 'Marsylia': {'Pole': 3444, 'Lokale': 56}, 'Leeds': {'Pole': 2952, 'Lokale': 44}, 'Frankfurt': {'Pole': 3515, 'Lokale': 57}, 'Genua': {'Pole': 3386, 'Lokale': 56}}

print(oniekt['Budapeszt']['Pole'])



thebestziom = ""
thebestwartosc = 0


for i in oniekt:
    if(oniekt[i]['Pole'] > thebestwartosc):
        thebestwartosc = oniekt[i]['Pole']
        thebestziom = [i,oniekt[i]]

print(thebestziom)



