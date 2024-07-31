file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

print(data)

thebestroznica = 0
thebestliczba = 0
for i in data:
    startowa  = int(i[0])
    liczba = int(i[0][::-1])
    if(abs(startowa-liczba) > thebestroznica):
        thebestroznica = abs(startowa-liczba)
        thebestliczba = startowa

print(thebestliczba,thebestroznica)
