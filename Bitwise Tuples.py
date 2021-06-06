t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    d=pow(2,a,1000000007)-1
    print(pow(d,b,1000000007))
