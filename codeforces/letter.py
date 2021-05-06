n,m=map(int,input().split())
mat=[]

for _ in range(n):
    s=input()
    a=list(s)
    mat.append(a)
Left=n-1
Right=0
Top=m-1
Bottom=0
for i in range(0,n):
    for j in range(0,m):
        if(mat[i][j]=='*'):
            Left=min(Left,i)
            Right=max(Right,i)
            Top=min(Top,j)
            Bottom=max(Bottom,j)
for i in range(Left,Right+1):
    for j in range(Top,Bottom+1):
        print(mat[i][j],end="")
    print(end="\n")
            
