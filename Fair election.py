n=int(input())
for i in range(n):
    v=0
    a,b=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    B=list(map(int,input().split()))
    B.sort(reverse=True)
    if(sum(A)>sum(B)):
        print("0")
    else:
        for j in range(len(B)):
            v=v+1
            A[j],B[j]=B[j],A[j]
            if(sum(A)>sum(B)):
                print(v)
                break
            elif(j<len(A)):
                continue
            elif(j==len(A)):
                print("-1")
        
