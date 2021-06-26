n=int(input())
for i in range(n):
    m=int(input())
    o=[]
    e=[]
    
    l=list(map(int,input().split()))
    for j in range(len(l)):
        if(l[j]%2==0):
            e.append(l[j])
        else:
            o.append(l[j])
    
    print(*(e+o))
