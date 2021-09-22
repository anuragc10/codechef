t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    tim=240
    marks=0
    m=max(x,y,z)
    if(m==x and tim>0):
        q=min(20,tim//a)
        t=q*a
        tim=tim-t
        marks=q*x
        m=max(z,y)
        if(m==y and tim>0):
            q=min(20,tim//b)
            t=q*b
            tim=tim-t
            marks=marks+q*y
            if(tim>0):
                q=min(20,tim//c)
                t=q*c
                tim=tim-t
                marks=marks+q*z
            elif(m==z and tim>0):
                q=min(20,tim//c)
                t=q*c
                tim=tim-t
                marks=marks+q*z
                if(tim>0):
                    q=min(20,tim//b)
                    t=q*b
                    tim=tim-t
                    marks=marks+q*y
    elif(m==y and tim>0):
        q=min(20,tim//b)
        t=q*a
        tim=tim-t
        marks=q*y
        m=max(x,z)
        if(m==x and tim>0):
            q=min(20,tim//a)
            t=q*a
            tim=tim-t
            marks=marks+q*x
            if(tim>0):
                q=min(20,tim//c)
                t=q*c
                tim=tim-t
                marks=marks+q*z
        elif(m==z and tim>0):
            q=min(20,tim//c)
            t=q*c
            tim=tim-t
            marks=marks+q*z
            if(tim>0):
                q=min(20,tim//a)
                t=q*a
                tim=tim-t
                marks=marks+q*x
    elif(m==z and tim>0):
        q=min(20,tim//c)
        t=q*c
        tim=tim-t
        marks=q*z
        m=max(x,y)
        if(m==y and tim>0):
            q=min(20,tim//b)
            t=q*b
            tim=tim-t
            marks=marks+q*y
            if(tim>0):
                q=min(20,tim//a)
                t=q*a
                tim=tim-t
                marks=marks+q*x
        elif(m==x and tim>0):
            q=min(20,tim//a)
            t=q*a
            tim=tim-t
            marks=marks+q*x
            if(tim>0):
                q=min(20,tim//b)
                t=q*b
                tim=tim-t
                marks=marks+q*y
    print(marks)
                
    
        
                
            
            
        
