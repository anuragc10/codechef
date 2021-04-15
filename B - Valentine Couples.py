t=int(input())
for _ in range(t):
    n=int(input())
    B=list(map(int,input().split()))
    G=list(map(int,input().split()))
    B.sort(reverse=True)
    G.sort()
    m=-1000
    for i in range(n):
        if((B[i]+G[i])>m):
            m=(B[i]+G[i])
    print(m)
        
