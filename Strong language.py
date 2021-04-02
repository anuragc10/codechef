t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=str(input())
    r=[]
    p=[]
    q=k*'*'
    for i,e in enumerate(s):
        substr=e*k;
        if(s[i:i+k]==substr):
            r.append(substr)
    p=list(set(r))
    if(q in p):
        print("Yes")
    else:
        print("No")
            
    
