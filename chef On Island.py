t=int(input())
for _ in range(t):
    x,y,xr,yr,d=map(int,input().split())
    d1=min((x/xr),(y/yr))
    if(d1>=d):
        print("Yes")
    else:
        print("No")
