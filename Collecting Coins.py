n=int(input())
for i in range(n):
    a,b,c,n=map(int,input().split())
    m=max(a,b,c)
    n=n-(m-a)
    n=n-(m-b)
    n=n-(m-c)
    a=m
    b=m
    c=m
    if(n>=0 and n%3==0):
        print("YES")
    else:
        print("NO")
