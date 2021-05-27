k=int(input())
l=list(map(int,input().split()))
n=len(l)
l.sort()

x=k
a=0
for i in range(n-1,-1,-1):
    if(x<=0):
        break
    else:
        a=a+1
        x=x-l[i]
if(x>0):
    print("-1")
else:
    print(a)

