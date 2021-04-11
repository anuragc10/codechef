t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in l:
        if(l.count(i)==1):
            print(l.index(i)+1)
            break
