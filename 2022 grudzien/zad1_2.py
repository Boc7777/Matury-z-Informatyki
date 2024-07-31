file = open("./Dane_2212/mecz.txt")
data = []
for l in file:
    data.append(l.strip())

data = data[0]

wynikA = 0
wynikB = 0
for i in data:
    if(i=="A"):
        wynikA+=1
    elif(i=="B"):
        wynikB+=1
    if(wynikA >=1000 or wynikB>=1000):
        if(abs(wynikA-wynikB) >=3):
            if(wynikA>wynikB):
                print(wynikA,wynikB,"wygranaA")
            else:
                print(wynikA,wynikB,"wygranaB")
