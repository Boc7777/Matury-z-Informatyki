file = open("gra.txt","r")
data=[]
for l in file:
    data.append(list(l.strip()))

for c in range(0,100):

    wysokosc = len(data)
    szerokosc = len(data[0])



    wielkitab = []


    #tworzenie giga taba
    for y in range(0,wysokosc+2):
        wiersz = []
        for x in range(0,szerokosc+2):
            wiersz.append("O")
        wielkitab.append(wiersz)


    #zmiana na giga taba
    for y in range(0,wysokosc+2):
        for x in range(0,szerokosc+2):


            prawo = False
            lewo = False
            gora = False
            dol = False

            if (x == 0):
                lewo = True
            if (x == szerokosc + 1):
                prawo = True
            if (y == 0):
                gora = True
            if (y == wysokosc + 1):
                dol = True

            if(gora and not lewo and not prawo ):
                wielkitab[y][x] = data[wysokosc-1][x-1]

            if (dol and not lewo and not prawo):
                wielkitab[y][x] = data[0][x-1]

            if (lewo and not gora and not dol):
                wielkitab[y][x] = data[y-1][szerokosc-1]

            if (prawo and not gora and not dol):
                wielkitab[y][x] = data[y-1][0]


            if(lewo and gora):
                wielkitab[y][x] = data[-1][-1]

            if (prawo and gora):
                wielkitab[y][x] = data[-1][0]

            if (lewo and dol):
                wielkitab[y][x] = data[0][-1]

            if (prawo and dol):
                wielkitab[y][x] = data[0][0]

            if( not gora and not dol and not lewo and not prawo):
                wielkitab[y][x] = data[y-1][x-1]



    # for i in wielkitab:
    #     print(i)

    nowytab = []

    #robienie nowego taba
    for y in range(1, wysokosc + 1):
        wiersz = []
        for x in range(1, szerokosc + 1):

            iloscsasiadow = 0

            if(wielkitab[y-1][x-1] == "X"):
                iloscsasiadow+=1
            if (wielkitab[y-1][x] == "X"):
                iloscsasiadow += 1
            if (wielkitab[y-1][x+1] == "X"):
                iloscsasiadow += 1


            if (wielkitab[y][x-1] == "X"):
                iloscsasiadow += 1
            if (wielkitab[y][x+1] == "X"):
                iloscsasiadow += 1


            if (wielkitab[y+1][x-1] == "X"):
                iloscsasiadow += 1
            if (wielkitab[y+1][x] == "X"):
                iloscsasiadow += 1
            if (wielkitab[y+1][x+1] == "X"):
                iloscsasiadow += 1



            if(wielkitab[y][x] == "X"):
                if(iloscsasiadow==2 or iloscsasiadow==3):
                    wiersz.append("X")
                else:
                    wiersz.append(".")

            if(wielkitab[y][x] == "."):
                if (iloscsasiadow == 3):
                    wiersz.append("X")
                else:
                    wiersz.append(".")

        nowytab.append(wiersz)


    print("---------------------------")
    for i in nowytab:
        print(i)

    suma = 0
    for i in nowytab:
        for a in i:
            if(a == "X"):
                suma+=1

    print(c+2,suma)
    data = nowytab






























