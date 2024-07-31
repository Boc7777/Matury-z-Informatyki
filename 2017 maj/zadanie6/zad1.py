file = open("dane.txt","r")

data = []

for l in file:
    data.append(l.strip().split(" "))

jasny = 0

ciemny = 300

for wiersz in data:
    for liczba in wiersz:
        liczba = int(liczba)
        if(liczba<ciemny):
            ciemny = liczba
        if(liczba> jasny):
            jasny = liczba
print("jasny:",jasny)
print("ciemny:",ciemny)