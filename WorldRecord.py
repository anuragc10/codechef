t=int(input())
for i in range(t):
    e=0
    f=0
    g=0
    a,b,c,d=map(float,input().split())
    e=a*b*c*d
    g=100/e
    f=round(g,2)
    if(f<9.58):
        print("Yes")
    else:
        print("No")
    
       
