n=int(input())
l=list(map(int,input().split()))
l.sort()
s=list(set(l))
c=0
x3=0
for i in range(len(s)):
    if(int(s[i])==0):
        i=i+1
    else:
        x=l.count(s[i])
        if(x>2):
            x3=1
            break
        else:
            if(x==2):
                c=c+1
            
if(x3==1):
    print("-1")
else:
    print(c)
