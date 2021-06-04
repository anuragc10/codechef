t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x=c//a
    y=d//b
    print(x+y)
