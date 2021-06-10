import math
n,t,k,d=map(int,input().split())
if(k>=n):
    print("NO")
else:
    c=math.ceil(n/k)
    s=t*c
    k=t+d
    if(s>k):
        print("YES")
    else:
        print("NO")
    
