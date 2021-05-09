n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
s=l[k-1]
for i in range(n):
    if(l[i]>=s and l[i]!=0):
        c=c+1
print(c)

