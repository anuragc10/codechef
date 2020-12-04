import math
n=int(input())
l1=[]
l2=[]
for i in range(n):
    N,d=map(int,input().split())
    l=list(map(int,input().split()))
    for j in l:
        if(j>=80 or j<=9):
            l1.append(j)
        else:
            l2.append(j)
    s=math.ceil(len(l1)/d)
    p=math.ceil(len(l2)/d)
    print(s+p)
    l1.clear()
    l2.clear()
    l.clear()
