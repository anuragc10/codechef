
t =int(input())
for _ in range(t):
    n=int(input())
    p=[]
    l=list(map(int,input().split()))
    l.insert(0,0)
    l.append(0)
    for i in range(1,n+1):
        c=0
        d=0
        
        for k in range(i-1,0,-1):
            if(l[i]!=l[k]):
                if(l[i]>l[k]):
                    continue
                else:
                    break
            else:
                d=d+1
        for j in range(i+1,n+1):
            if(l[i]!=l[j]):
                if(l[i]>l[j]):
                    continue
                else:
                    break
            else:
                c=c+1
        p.append(c+d)
    print(*p)
    p.clear()
