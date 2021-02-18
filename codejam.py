n=int(input())

for i in range(n):
    N,k,s=map(int,input().split())
    a=k-1
    res=N+1
    tres=a+res
    p=k-s
    h=N-s+1
    t=p+h+a
    if(t>tres):
        print("Case #"+str(i+1)+": "+str(tres))
    else:
        print("Case #"+str(i+1)+": "+str(t))
    
