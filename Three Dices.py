t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=a+b
    if(c>=6):
        print(0)
    else:
        d=6-c
        d=d/6
        print(d)
