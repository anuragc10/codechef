p=int(input())
l=[]
a1,b1,c1,d1=map(int,input().split())
a2,b2,c2,d2=map(int,input().split())
a3,b3,c3,d3=map(int,input().split())
a4,b4,c4,d4=map(int,input().split())

a11=min(a1,b1)+ min(c1,d1)
a22=min(a2,b2)+ min(c2,d2)
a33=min(a3,b3)+ min(c3,d3)
a44=min(a4,b4)+ min(c4,d4)

l.append(a11)
l.append(a22)
l.append(a33)
l.append(a44)

a=1000
for i in range(4):
    if(l[i]<=p):
        a=i
        break
    else:
        a=1000
if(a==0):
    print(a+1,min(a1,b1),p-min(a1,b1))
elif(a==1):
    print(a+1,min(a2,b2),p-min(a2,b2))
elif(a==2):
    print(a+1,min(a3,b3),p-min(a3,b3))
elif(a==3):
    print(a+1,min(a4,b4),p-min(a4,b4))
else:
    print("-1")
