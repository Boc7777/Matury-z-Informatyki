
A = [4,34,16,8,22,14,12,2,7]
n = len(A)
p = 2

jedna = 0
druga = 0
for i in range(0,n):
    if(A[i]%p!=0):
        if(A[i]>jedna and A[i]>druga):
            if(jedna>druga):
                druga=A[i]
            else:
                jedna=A[i]
        elif(A[i]<jedna and A[i]>druga):
            druga = A[i]
        elif (A[i] > jedna and A[i] < druga):
            jedna = A[i]
print(jedna*druga)


