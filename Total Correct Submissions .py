# cook your dish here
n=int(input())
for i in range(n):
    m=int(input())
    l=[]
    l1=[0]*3*m
    c=-1
    for i in range(3*m):
        a,b=map(str,input().split())
        if(a in l):
            
            l1[c]=l1[c]+int(b)
        else:
            l.append(a)
            c=c+1
            l1[c]=l1[c]+int(b)
            
    d=0
    l2=[]
    for i in range(len(l1)):
        if(l1[i]!=0):
            l2.append(l1[i])
    l2.sort()
    print(*l2)
    
    
    ////
    
    n=int(input())
for i in range(n):
    m=int(input())
    l=[]
    l1=[]
    l2=[]
    for i in range(3*m):
        a,b=map(str,input().split())
        l1.append(a)
        l2.append(b)
    c=int(l2[0])
    for i in range(0,len(l1)-1):
        if(l1[i]==l1[i+1]):
            c=c+int(l2[i+1])
        else:
            l.append(c)
            c=int(l2[i+1])
    l.append(c)
    l.sort()
    print(*l)
