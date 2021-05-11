n=int(input())
l=list(map(int,input().split()))
m=n//2
s=sum(l)//m
for i in range(n):
    for j in range(n):
        if(i!=j):
            if(l[i]+l[j]==s):
                print(i+1,j+1)
                l[i]=0
                l[j]=0
