t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    sa=[]
    sb=[]
    if(sum(h)<2*k):
        print("-1")
    elif(sum(h)==2*k):
        print(len(h))
    else:
        t=0
        i=0
        while(i<n):
            sa.append(h[i])
            if(sum(sa)>=k):
                break
            else:
                for j in range(i+1,n):
                    if(h[j]>=(k-sum(sa))):
                        t=1
                        break
                if(t==1):
                    sa.append(h[j])
                    h[j],h[i+1]=h[i+1],h[j]
        m=0
        i=i+1
        while(i<n):
            sb.append(h[i])
            if(sum(sb)>=k):
                break
            else:
                for j1 in range(i+1,n):
                    if(h[j1]>=(k-sum(sb))):
                        m=1
                        break
                if(m==1):
                    sb.append(h[j])
                    h[j1],h[i+1]=h[i+1],h[j1]
                if(m!=1):
                    for j in range(i+1,n):
                        if(a[m]<(k-sum(sb))):
                            break
                    h[m],h[i+1]=h[i+1],h[m]
        print(i)
