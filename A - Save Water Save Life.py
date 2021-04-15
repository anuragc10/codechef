t=int(input())
for _ in range(t):
    H,x,y,C=map(int,input().split())
    p=(x+y//2)*H
    if(p<=C):
        print("YES")
    else:
        print("NO")
