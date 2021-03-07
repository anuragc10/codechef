n=int(input())
for i in range(n):
    c=0
    x=0
    k=int(input())
    A=list(map(int,input().split()))
    A.sort()
    for j in range(k):
        if(A[j]>(j+1)):
            print("Second")
            x=1
            break
    if(x==0):
        for p in range(k):
            c=c+abs(A[p]-(p+1))
        if(c%2==0):
            print("Second")
        else:
            print("First")
