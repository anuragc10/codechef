a,b=map(int,input().split())
s=0
t=0
while(b):
    t=b
    s=s+a//b
    b=a%b
    a=t

print(s)
