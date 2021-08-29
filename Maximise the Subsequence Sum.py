t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    p=[]
    ans=0
    l=list(map(int,input().split()))
    for i in range(n):
        if(l[i]<0):
            p.append(l[i])
        else:
            ans=ans+l[i]
    c=0
    a=k
    p.sort()
    if(k>=len(p)):
        k=len(p)
    while(k):
        p[c]=p[c]*(-1)
        k=k-1
        c=c+1
    a2=sum(p[:a])
    ans=ans+a2
    print(ans)
    
