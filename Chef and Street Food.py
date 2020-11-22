n=int(input())
for _ in range(n):
    i=int(input())
    ans=0
    for p in range(i):
        s,v,p=(map(int,input().split()))
        ans=max(ans,v*(p//(s+1)))
        
    print(ans)
