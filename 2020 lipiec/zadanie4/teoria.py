# n = 9
# P = []
# S = []
#
# for i in range(0,11):
#     P.append(1)
#     S.append(0)
#
# for j in range(2,10):
#     if(P[j] == 1):
#         i = j*j
#         while i<=10:
#             P[i] = 0
#             i = i + j
#     S[j] = S[j-1]+P[j]
#
# print(S)

def funkcja(n):
    print("wywołanie")
    if(n==0):
        return 1
    else:
        s = 1
        for i in range(0,n):
            s = s + funkcja(i)
        return s

print(funkcja(2))
