import math
n=int(input())
l=list(map(int,input().split()))
c=0
d=0
a=math.ceil(n/2)
for i in l:
    if(i>0):
        c=c+1
    if(i<0):
        d=d+1
if(c>=a):
    print("1")
elif(d>=a):
    print("-1")
else:
    print("0")
