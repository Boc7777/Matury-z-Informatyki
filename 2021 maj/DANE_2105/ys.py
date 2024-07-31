file = open('instrukcje.txt', 'r')
data=[]
wynik=[]
alfabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciag=0
thebestciag=0
aktualnanazwa=""
thebestnazwa=""
sprawdzana = ""
for line in file:
    data.append(line.strip().split(" "))


for i,element in enumerate(data):
    if i+1 != len(data):
        print(element)
        ciag=0
        aktualnanazwa = element[0]
        sprawdzana =data[i+1][0]
        print(sprawdzana)
        x = 0
        while(aktualnanazwa==sprawdzana):
            ciag+=1
            sprawdzana = data[i+ciag][0]

        if(ciag> thebestciag):
            thebestciag = ciag
            thebestnazwa = aktualnanazwa
print(thebestnazwa,thebestciag)