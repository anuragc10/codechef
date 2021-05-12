n,k=map(int,input().split())
t=240-k 
c=0
i=1
while(1):
    c=c+i*5
    if(c<=t and i<=n):
        i=i+1
    else:
        print(i-1)
        break
