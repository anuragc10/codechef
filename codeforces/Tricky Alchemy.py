Y,B=map(int,input().split())
x,y,z=map(int,input().split())
reqA=2*x+y
reqB=y+3*z
res=0

if(reqA>Y):
    res=res+reqA-Y
if(reqB>B):
    res=res+reqB-B
print(res)
