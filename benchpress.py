for _ in range(int(input())):
    n,w,wr=map(int,input().split())
    l=list(map(int,input().split()))
    s1=list(set(l))
    m=0
    s=wr
    if(wr>=w):
        print('Yes')
    else:
        for i in range(len(s1)):
            c=0
            c=l.count(s1[i])
            if(c%2==0):
                s=wr+c*s1[i]
            else:
                s=wr+(c-1)*s1[i]
            if(s>=w):
                m=1
                break
        if(m==1):
            print('Yes')
        else:
            print('No')
