# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    p=y-x
    q=z*2
    if(p<=0):
        print("YES")
    else:
        if(q>=p):
            print("YES")
        else:
            print("NO")
