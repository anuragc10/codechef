n,k=(map(int,input().split()))
c=0
for i in range(n):
    m=int(input())
    if(m%k==0):
        c=c+1
print(c)
