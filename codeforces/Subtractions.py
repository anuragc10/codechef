t=int(input())
for _ in range(t):
    c=0
    a,b=map(int,input().split())
    while(a!=0 and b!=0):
        if(a<b):
            a,b=b,a
        c=c+a//b
        a=a%b
    print(c)
