t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    if(((n+1)-x)%k==0 or x%k==0):
        print("Yes")
    else:
        print("No")
