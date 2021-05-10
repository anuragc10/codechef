
s=0
n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
if(a>b):
    a,b=b,a
for i in range(a-1,b-1):
    s=s+l[i]
x=(sum(l)-s)
if(s<=x):
    print(s)
else:
    print(x)

