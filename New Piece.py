t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x=0
    y=0
    if((a+b)%2==0):
        x=1
    if((c+d)%2==0):
        y=1
    if(a==c and b==d):
        print("0")
    else:
        if((x==1 and y==1) or (x==0 and y==0)):
            print("2")
        else:
            print("1")
