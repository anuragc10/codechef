n=int(input())
l=[]
a=[]
b=[]
for i in range(n):
    p=int(input())
    for j in range(p):
        l=list(map(int,input().split()))
        l.sort(reverse=True)
        for k in l:
            if(len(a)==0 and len(b)==0):
                a.append(k)
            elif(len(a)!=0 and len(b)==0):
                b.append(k)
            elif(len(a)!=0 and len(b)!=0):
                if(sum(a)>=sum(b)):
                    b.append(k)
                else:
                    a.append(k)
        if(sum(a)>=sum(b)):
            print(sum(a))
        else:
            print(sum(b))
        l.clear()
        a.clear()
        b.clear()
