n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q//2):
    l2=list(map(int,input().split()))
    L=l2[1]
    R=l2[2]
    x=l2[3]
    a,b=map(int,input().split())

    for j in range(L-1,R):
        l[j]=l[j]+(x)**2
        x=x+1
    print(l[b-1])
