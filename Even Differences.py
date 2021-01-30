n=int(input())
for i in range(n):
    e=0
    o=0
    m=int(input())
    l=list(map(int,input().split()))
    for j in l:
        if(j%2==0):
            e=e+1
        else:
            o=o+1
    
    n=0
    if(o!=0 and e!=0):
        if(o>e):
            n=e
        else:
            n=o
    print(n)
            
    
