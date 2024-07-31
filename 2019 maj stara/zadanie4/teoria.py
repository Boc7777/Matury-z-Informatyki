plik = open("siema.txt","w")

plik.writelines("[1,2,3,4,56,6]\n")
plik.writelines("s")

plik.close()

a  = 2
k  = 7

def pot(a,k):
    startowa = a
    for i in range(1,k):
        a = a*startowa
    return a%k





def testF(k):
    czygit = True
    for a in range(2,k):
        if(pot(a,k) != a):
            czygit = False
    if(czygit):
        return 1
    else:
        return 0


print(testF(4))