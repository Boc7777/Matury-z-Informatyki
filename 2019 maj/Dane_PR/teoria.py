A = [5,3,3,3,5,3,3,3,8, 4, 24, 4, 8]
n = len(A)

def szukanie(A,n):
    for i in range(0,n):
        if(A[i]%2==0):
            return A[i]
# print(szukanie(A,n))




def szukanie2(A,m,n):

    s = (m+n)//2
    if (n - m != 1):
        if(A[s]%2==0):
            return szukanie2(A, m, s)
        else:
            return szukanie2(A, s, n)
    else:
        return A[n]


print(szukanie2(A,0,n))






