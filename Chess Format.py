t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(a+b<3):
        print(1)
    if(a+b>2 and a+b<11):
        print(2)
    if(a+b>10 and a+b<61):
        print(3)
    if(a+b>60):
        print(4)
