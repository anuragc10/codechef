t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    T=(n-x)+(m-y)
    P=max(n-a,m-b)
    if(T<=P):
        print("Yes")
    else:
        print("No")
    
