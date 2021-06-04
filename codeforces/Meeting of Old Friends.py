l1,r1,l2,r2,k=map(int,input().split())
a=max(l1,l2)
b=min(r1,r2)
c=b-a+1
if(k<=b and k>=a):
    c=c-1
if(c<0):
    print(0)
else:
    print(c)

