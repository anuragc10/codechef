t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    for k in range(m):
        c=0
        a,b=map(int,input().split())
        m2=l[b-1]
        for j in range(b-1,n):
            if(l[j]>m2):
                m2=l[j]
                c=c+1
        print(c)
