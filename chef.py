n=int(input())
for i in range(n):
    c=0
    A=str(input())
    for j in range(len(A)):
        if(j<len(A)-1 and j>0):
            if(A[j]=='1'):
                if(A[j-1]=='0'):
                    c=c+1
                if(A[j-1]=='1'):
                    c=c+0
            else:
                continue
        elif(j==len(A)-1):
            if(A[j]=='1' and A[j-1]=='1'):
                c=c+0
            elif(A[j]=='1' and A[j-1]=='0'):
                c=c+1
        elif(j==0):
            if(A[j]=='1'):
                c=c+1
            else:
                continue
            
    print(c)
