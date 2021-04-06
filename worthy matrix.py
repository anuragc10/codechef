
t=int(input())
def fun(mat,n,m,k,o):
    count=0
    ans=0
    minimum=min(n,m)
    while(o<(minimum+1)):
        i=o
        j=m
        while(i<(n+1)):
            x=i-o+1
            y=j-o+1
            z=mat[i][j]-mat[x-1][j]-mat[i][y-1]+mat[x-1][y-1]
            if((z/(o*o))<k):
                i+=1
            else:
                start=o
                end=m
                while(start<=end):
                    mid=(start+end)//2
                    x=i-o+1
                    y=mid-o+1
                    z=mat[i][mid]-mat[x-1][mid]-mat[i][y-1]+mat[x-1][y-1]
                    if((z/(o*o))<k):
                        start=mid+1
                    else:
                        ans=mid
                        end=mid-1
                count+=m-ans+1
                i+=1
        o=o+1
    return count
                        
                

    
for _ in range(t):
    mat=[]
    n,m,k=map(int,input().split())
    for r1 in range(n):
        l=[]
        l=list(map(int,input().split()))
        mat.append(l)

    for i1 in range(m):
        s=0
        for j1 in range(n):
            s+=mat[i1][j1]
            mat[i1][j1]=s
    for i2 in range(m):
        s=0
        for j2 in range(m):
            s+=mat[i2][j2]
            mat[i2][j2]=s
    
    for i3 in range(m):
        mat[i3].insert(0,0)
    
    q=[0]*(n+1)
    mat.insert(0,q)
    
    Ans=fun(mat,n,m,k,1)
    print(Ans)

   
    
        
            
    

 

    
 
        
