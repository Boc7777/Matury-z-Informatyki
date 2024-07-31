file = open('instrukcje.txt')

data = []

for l in file:
    data.append(l.strip().split(" "))


nazwainstrukcji = ""
maxdlugosc = 0

aktualnanazwa = ""
aktualnadlugosc = 0

for kom in data:
    if(kom[0] == aktualnanazwa):
        aktualnadlugosc+=1
    else:
        aktualnanazwa = kom[0]
        aktualnadlugosc = 1


    if(aktualnadlugosc > maxdlugosc):
        maxdlugosc = aktualnadlugosc
        nazwainstrukcji = aktualnanazwa

print(nazwainstrukcji,maxdlugosc)