k = 5
x = 16
y = 30


def ilejesttimkow(n):
    return 2**n

interwal =  ilejesttimkow(k)
ilosctimkow = ilejesttimkow(k)
znaleziono = False
start = 0
koniec = ilejesttimkow(k)
a = 0

while interwal>2:
    interwal = interwal / 2
    i = interwal
    while i <= ilosctimkow:

        if((x >= (i-interwal) and x<i) and (y >= (i-interwal) and y<i)):
            print("do przedział : ",(i-interwal),"do: ",i, "naleza:",x,y )
            a +=1
        else:
            print("do przedział: ",(i-interwal),"do: ",i, " nie naleza:",x,y )
        print(i)
        i+=interwal
print(k-a)


