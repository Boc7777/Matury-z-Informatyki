Czyjest =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

n = 100
k = 75

def Sitko(n):
    for i in range(1,n):
        Czyjest[i] = False
    j = 1
    while j*j<n:
        j+=1
    suma = 0
    for i in range(2,j):



        kw = i*i
        poz = kw
        while poz <= n:
            suma+=1
            Czyjest[poz] = True
            poz = poz+kw


Sitko(n)

print(int("00010110100",2))
print(int("000330",4))
print(int("078",16))


print("-----------------")

print(int("00011010010",2))
print(int("001122",4))
print(int("096",16))














