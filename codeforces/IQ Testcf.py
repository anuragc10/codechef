l=[]

for _ in range(4):
    s=input()
    a=list(s)
    l.append(a)


e=0
for i in range(3):
    for j in range(3):
        c=0
        d=0
        if(l[i][j]=="#"):
            c=c+1
        else:
            d=d+1
        if(l[i][j+1]=="#"):
            c=c+1
        else:
            d=d+1
        if(l[i+1][j+1]=="#"):
            c=c+1
        else:
            d=d+1
        if(l[i+1][j]=="#"):
            c=c+1
        else:
            d=d+1

        if(d>=3 or c>=3):
            e=1
            break

if(e==1):
    print("YES")
else:
    print("NO")
