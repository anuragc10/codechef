# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a=l[0]+l[1]+l[2]
    b=l[3]+l[4]+l[5]
    if(a>b):
        print("1")
    else:
        print("2")
