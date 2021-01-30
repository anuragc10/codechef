n=int(input())
for i in range(n):
    c=0
    m,a=map(int,input().split())
    l=list(map(int,input().split()))
    for j in range(m):
        for k in range(m):
            if((l[j]+l[k])%a==0):
                c=c+1
                break
            else:
                continue
    if(c!=len(l)):
        print("NO")
    else:
        print("YES")
          
