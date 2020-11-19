n=int(input())
for i in range(n):
    count=0
    p=int(input())
    l=list(map(int,input().split()))
    c=l[0]
    for q in l:
        if(q<=c):
            c=q
            count=count+1
    print(count)
