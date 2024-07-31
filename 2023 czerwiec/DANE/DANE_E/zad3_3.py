file = open("anagram.txt","r")
data = []

for l in file:
    data.append(l.strip().split(" "))


tab = []
for index, i in enumerate(data):
    if(index+1 != len(data)):
        roznica = abs( int(data[index][0],2)- int(data[index+1][0],2) )
        print(roznica)
        tab.append(roznica)


print(max(tab) )
print(bin(max(tab)) )