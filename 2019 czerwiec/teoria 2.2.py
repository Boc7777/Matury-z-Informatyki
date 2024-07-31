k = 10
n = 40
S = "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"

liczbapodziału = n/k

tab = []

for i in range(0,k):
    start = int(i*liczbapodziału)
    koniec = int((i+1)*liczbapodziału)
    zestaw = S[start:koniec:1]
    tab.append(zestaw)

T = ""


for i in range(1,int(liczbapodziału)+1):
    #nieparzyste z góry na dół
    if(i%2 == 1):
        for a in range(0,k):
            T+=tab[a][i-1]

    else:
        for a in reversed(range(0,k)):
            T+=tab[a][i - 1]




print(T)