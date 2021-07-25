import math
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=0
    while(a>0):
       a=math.floor(a/b)
       c=c+1
    print(c)
