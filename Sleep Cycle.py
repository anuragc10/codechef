# cook your dish here
t=int(input())
for _ in range(t):
    L,h=map(int,input().split())
    s=input()
    l=[]
    a=[]
    c=0
    for i in range(L):
        if(s[i]=='0' and i!=L-1):
            c=c+1
        elif(s[i]=='0' and i==L-1):
            c=c+1
            a.append(c)
        elif(i==L-1 or s[i]=='1'):
            a.append(c)
            c=0
    d=0
    for j in range(len(a)):
        p=2*(h-a[j])
        if(p>=h):
            j=j+1
        else:
            h=p
        if(h<=0):
            d=1
            print("YES")
            break
    if(d==0):
        print("NO")
    
         
