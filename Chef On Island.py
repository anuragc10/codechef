t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    lis=[]
    for j in range(n):
        score=input()
        l=list(score)
        if(l.count("F")>=x):
            lis.append("1")
        elif(l.count("F")>=x-1 and l.count("P")>=y):
            lis.append("1")
        else:
            lis.append("0")
    print("".join(lis))
