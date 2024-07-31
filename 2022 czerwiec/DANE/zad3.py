file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

print(data)

def czypierwsza(liczba):
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True



for i in data:
    startowa = int(i[0])
    odbicie = int(i[0][::-1])
    if(czypierwsza(startowa) and czypierwsza(odbicie)):
        print(startowa)