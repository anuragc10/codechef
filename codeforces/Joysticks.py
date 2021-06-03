a,b=map(int,input().split())
ans=0
while(a>0 and b >0):
    if(a>b):
        a,b=b,a
    a=a+1
    b=b-2
    ans=ans+1
    if(a<0 or b<0):
        ans=ans-1
        break
print(ans)
