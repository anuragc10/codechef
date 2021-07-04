t=int(input())
for _ in range(t):
    d,x,y,z=map(int,input().split())
    a=7-d
    b=7*x
    c=y*d+z*a
    print(max(b,c))
