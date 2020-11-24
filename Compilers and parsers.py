n=int(input())
for _ in range(n):
    m=input()
    l=[]
    count=0
    ans=0
    for i in m:
        count+=1
        if i=="<":
            l.append(i)
        elif i==">":
            if len(l)==0:
                break
            elif l[len(l)-1]=="<":
                l.pop()
                if len(l)==0:
                    ans=count
            else:
                break
    print(ans)
