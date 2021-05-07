t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=b+(100-a)*c
    print(x*10)
