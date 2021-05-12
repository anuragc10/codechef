n,m=map(int,input().split())
i=1
j=2
while(1):
    if(i%2!=0):
        n=n-i
        i=i+1
    else:
        m=m-i
        i=i+1
    if(n<0):
        print('Vladik')
        break
    if(m<0):
        print('Valera')
        break
        
        
    
