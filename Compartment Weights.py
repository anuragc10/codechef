n=int(input())
for i in range(n):
    s=0
    m=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    for j in range(int(input())):
        S,E,W=map(int,input().split())
        s=s+W*(E-S+1)
    print(s)
