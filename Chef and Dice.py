t=int(input())
for i in range(t):
    n=int(input())
    if(n==1):
        print(20)
    elif(n==2):
        print(36)
    elif(n==3):
        print(51)
    elif(n==4):
        print(60)
    else:
        c=0
        c=n//4 *44
        p=n%4
        if(p==0):
            c=c+16
        if(p==1):
            c=c+32
        if(p==2):
            c=c+44
        if(p==3):
            c=c+55;
        print(c)
    
