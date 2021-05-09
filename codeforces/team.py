n=int(input())
d=0
for i in range(n):
    a,b,c=map(int,input().split())
    if(a+b+c>1):
        d=d+1
print(d)
