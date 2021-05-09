n,m=map(int,input().split())
c=0
for a in range(n+m):
    for b in range(m+n):
        if(a**2+b==n and b**2+a==m):
            c=c+1
print(c)
