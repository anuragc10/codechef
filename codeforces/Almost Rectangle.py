t=int(input())
for _ in range(t):
    n=int(input())
    matrix=[]
    l=[]
    for i in range(n):          # A for loop for row entries
        a =input()
        matrix.append([str(p) for p in a])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                l.append(i)
                l.append(j)
    x1,y1=l[0],l[1]
    x2,y2=l[2],l[3]

    if(x1==x2):
        if(x1==(n-1)):
            matrix[x1-1][y1]="*"
            matrix[x2-1][y2]="*"
        else:
            matrix[x1+1][y1]="*"
            matrix[x2+1][y2]="*"
            
    if(y1==y2):
        if(y1==(n-1)):
            matrix[x1][y1-1]="*"
            matrix[x2][y2-1]="*"
        else:
            matrix[x1][y1+1]="*"
            matrix[x2][y2+1]="*"

    if(x1!=x2 and y1!=y2):
        matrix[x1][y2]="*"
        matrix[x2][y1]="*"
        

    for k in range(len(matrix)):
        print(*matrix[k],sep='')
    
    
    
