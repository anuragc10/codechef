n=int(input())
l=list(map(int,input().split()))
a=[]
l.reverse()
for i in range(n):
    if(l[i] not in a):
        a.append(l[i])
a.reverse()
print(len(a))
print(*a)
