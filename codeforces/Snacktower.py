n=int(input())
l=list(map(int,input().split()))
w=[0]*100001
p=n
d=0
for i in range(n):
    c=l[d]
    w[c]=1
    while(p>0 and w[p]==1):
        print(p,end="")
        p=p-1
    print("")
    d=d+1
    
