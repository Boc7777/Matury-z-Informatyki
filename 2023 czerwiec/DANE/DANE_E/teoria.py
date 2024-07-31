file = open("slowa3.txt","r")
data = []
for l in file:
    data.append(l.strip().split())
print(data)

def czy_mniejszy(n,s,k1,k2):
    s = list(s[0])
    i = k1-1
    j = k2-1
    while i<=n and j<=n:
        if(s[i] == s[j]):
            i+=1
            j+=1
        else:
            if(s[i] < s[j]):
                return True
            else:
                return False
    if(j<=n):
        return True
    else:
        return False




print(czy_mniejszy(   int(data[0][0])-1,  data[1],   int(data[2][0]),   int(data[2][1])) )