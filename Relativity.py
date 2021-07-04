t=int(input())
for _ in range(t):
    g,c=map(int,input().split())
    c=c*c
    g=2*g
    print(c//g)
