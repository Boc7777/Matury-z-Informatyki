file = open("liczby.txt","r")
data = []
for l in file:
    data.append(l.strip().split(" "))

print(data)


for i in data:
    liczba = int(i[0][::-1])
    if(liczba%17==0):
        print(liczba)