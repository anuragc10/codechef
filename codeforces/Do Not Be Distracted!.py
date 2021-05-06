t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=list(s)
    c=0
    for i in range(1,n):
        if(l[i]==l[i-1]):
            i=i+1
        else:
            for j in range(i,n):
                if(l[i-1]==l[j]):
                    c=1
                else:
                    j=j+1
    if(c==0):
        print("YES")
    else:
        print("NO")
