import math
a,b,c=map(int,input().split())
while(1):
    x=math.gcd(a,c)
    c=c-x
    if(c==0):
        print(0)
        break
    x=math.gcd(b,c)
    c=c-x
    if(c==0):
        print(1)
        break
