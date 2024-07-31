file = open("napisy.txt","r")
data = []
for l in file:
    data.append(list(l.strip()))

napis = ""
indexlitery = 0
for index, i in enumerate(data):
    if((index+1)%20 == 0 and index!=0):
        napis+=data[index][indexlitery]
        indexlitery+=1

print(napis)