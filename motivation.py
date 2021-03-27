t =int(input())
for _ in range(t):
    c=0
    d=0
    n,x=map(int,input().split())
    for p in range(n):
        s,r=map(int,input().split())
        if(x>=s):
            d=max(d,r)
    print(d)
 
