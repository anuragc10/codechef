t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    su=(n*(n+1))//2
    if(su>s):
        if((su-s)<=n):
            print(su-s)
        else:
            print(-1)
    else:
        print(-1)
