t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    tim=240
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    
    if(tim>0):
        q=min(20,tim//a)
        t=q*a
        tim=tim-t
        m1=q*x
        if(tim>0):
            q=min(20,tim//b)
            t=q*b
            tim=tim-t
            m1=m1+q*y
            if(tim>0):
                q=min(20,tim//c)
                t=q*c
                tim=tim-t
                m1=m1+q*z
    tim=240

    if(tim>0):
        q=min(20,tim//a)
        t=q*a
        tim=tim-t
        m2=q*x
        if(tim>0):
            q=min(20,tim//c)
            t=q*c
            tim=tim-t
            m2=m2+q*z
            if(tim>0):
                q=min(20,tim//b)
                t=q*b
                tim=tim-t
                m2=m2+q*y
    if(tim>0):
        q=min(20,tim//b)
        t=q*b
        tim=tim-t
        m3=q*y
        if(tim>0):
            q=min(20,tim//a)
            t=q*a
            tim=tim-t
            m3=m3+q*x
            if(tim>0):
                q=min(20,tim//c)
                t=q*c
                tim=tim-t
                m3=m3+q*z
    tim=240

    if(tim>0):
        q=min(20,tim//b)
        t=q*b
        tim=tim-t
        m4=q*y
        if(tim>0):
            q=min(20,tim//c)
            t=q*c
            tim=tim-t
            m4=m4+q*z
            if(tim>0):
                q=min(20,tim//b)
                t=q*b
                tim=tim-t
                m4=m4+q*y
    tim=240

    if(tim>0):
        q=min(20,tim//c)
        t=q*c
        tim=tim-t
        m5=q*z
        if(tim>0):
            q=min(20,tim//a)
            t=q*a
            tim=tim-t
            m5=m5+q*x
            if(tim>0):
                q=min(20,tim//b)
                t=q*b
                tim=tim-t
                m5=m5+q*y
    tim=240

    if(tim>0):
        q=min(20,tim//c)
        t=q*c
        tim=tim-t
        m6=q*z
        if(tim>0):
            q=min(20,tim//b)
            t=q*b
            tim=tim-t
            m6=m6+q*y
            if(tim>0):
                q=min(20,tim//a)
                t=q*a
                tim=tim-t
                m6=m6+q*x
    print(max(m1,m2,m3,m4,m5,m6))