n,d=map(int,input().split())
s=input()
l=[]
for i in range(n):
    if(s[i]=='1'):
        l.append(i)

c=0
a=0
for i in range(0,len(l)):
    if(l[i]-c > d):
        print("-1")
        break
    while((i < len(l)) and (l[i]-c<=d)):
        i=i+1
    if(i==len(l)):
        print(a+1)
        break
    else:
        c=l[i-1]
        a=a+1
    
