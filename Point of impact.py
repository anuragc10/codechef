for i in range(int(input())):
    l=dict()
    n,K,x,y=map(int,input().split())
    p=K%4
    if(x==y):
        print(str(n)+","+str(n))
    if(x>y):
        l[0]=n,n-x+y
        l[1]=n-x+y,n
        l[2]=0,x-y
        l[3]=x-y,0
        if(p==0):
            print(*l[3])
        else:
            print(*l[p-1])
    if(x<y):
        l[0]=n+x-y,n
        l[1]=n,n+x-y
        l[2]=y-x,0
        l[3]=0,y-x
        if(p==0):
            print(*l[3])
        else:
            print(*l[p-1])
        
        
