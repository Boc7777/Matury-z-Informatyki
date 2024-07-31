n=32

rozklad = 0


def szukanie(n):
    znaleziona = True
    i=1
    while znaleziona:
        if(i*i>n):
            znaleziona= False
            return(i-1)
        i = i+1



while n>0:
    rozklad = rozklad+1
    potega = szukanie(n)
    n = n - (potega*potega)

print(rozklad)
