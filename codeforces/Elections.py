import statistics
from statistics import mode
n,m=map(int,input().split())
w=[]
for _ in range(m):
    l=list(map(int,input().split()))
    m=max(l)
    for i in range(n):
        if(l[i]==m):
            a=i
            break
    w.append(a+1)
w.sort()
    
print(mode(w))
