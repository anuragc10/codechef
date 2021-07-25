t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    
    if(a==b):
        print(0)
    else:
        d=b-a
        print((d//2)+1)
    
# cook your dish here
