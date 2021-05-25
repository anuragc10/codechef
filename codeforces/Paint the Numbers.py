n=int(input())
c=0
l=list(map(int,input().split()))
l.sort()
for i in range(0,n):
    d=1
    for j in range(0,i):
        if(l[i]%l[j]==0):
            d=0
    c=c+d
print(c)
        
