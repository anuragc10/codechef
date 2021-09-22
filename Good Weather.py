t=int(input())
for _ in range(t):
    d=0
    c=0
    l=list(map(int,input().split()))
    for i in l:
        if(i==1):
            c=c+1
        else:
            d=d+1
    if(c>d):
        print("YES")
    else:
        print("NO")
