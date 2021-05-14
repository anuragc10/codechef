import math
a=int(input())
b=int(input())
d=abs(a-b)
if(d<=2):
    print(d)
else:
    x=math.ceil(d/2)
    y=d-x
    g=(x*(x+1))//2+(y*(y+1))//2
    print(g)
