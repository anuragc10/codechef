t =int(input())
for _ in range(t):
    
    u,v,a,s=map(int,input().split())
    d=u*u - 2*a*s
    if(d<=v**2):
        print("Yes")
    else:
        print("No")
