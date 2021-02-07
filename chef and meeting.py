n=int(input())

for k in range(n):
    h,m=0,0
    A=[]
    t=str(input())
    h=int(t[0:2])
    m=int(t[3:5])
    if(t[6:8]=='AM' and h==12):
        h=h-12
    elif(t[6:8]=='PM' and h!=12):
        h=h+12

    a=int(input())
    for j in range(a):
        h1,h2,m1,m2=0,0,0,0
        t1=str(input())
        h1=int(t1[0:2])
        m1=int(t1[3:5])
        if(t1[6:8]=='AM' and h1==12):
            h1=h1-12
        elif(t1[6:8]=='PM' and h1!=12):
            h1=h1+12
        h2=int(t1[9:11])
        m2=int(t1[12:14])
        if(t1[15:17]=='AM' and h2==12):
            h2=h2-12
        elif(t1[15:17]=='PM' and h2!=12):
            h2=h2+12

                    
        if(h>h1 and h<h2):
            A.append(1)
        elif(h==h1 and h<=h2):
            if(m>=m1):
                A.append(1)
            else:
                A.append(0)
        elif(h>=h1 and h==h2):
            if(m<=m2):
                A.append(1)
            else:
                A.append(0)
        else:
             A.append(0)
              
            
        
    print(''.join(str(x) for x in A))
    

        
