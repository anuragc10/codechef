t=int(input())
for _ in range(t):
    D,d,p,q=map(int,input().split())
    c=0
    x=D//d
    if(x%2==0):
        c=c+d*(x//2)*(2*p+(x-1)*q)
    else:
        c=c+d*(x*(p+((x-1)//2)*q))
    c=c+(D%d)*(p+x*q)
    print(c)
        
        
