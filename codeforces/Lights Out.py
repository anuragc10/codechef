l=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

a=[[1,1,1,1,1]]
for _ in range(3):
    q=list(map(int,input().split()))
    q.insert(0,1)
    q.append(1)
    a.append(q)
a.append([1,1,1,1,1])

for i in range(1,4):
    for j in range(1,4):
        if(a[i][j]%2==1):
            l[i][j]=abs(1-l[i][j])
            l[i+1][j]=abs(1-l[i+1][j])
            l[i][j+1]=abs(1-l[i][j+1])
            l[i-1][j]=abs(1-l[i-1][j])
            l[i][j-1]=abs(1-l[i][j-1])
for k in range(1,4):
    for p in range(1,4):
        print(l[k][p],end="")
    print("")
            
