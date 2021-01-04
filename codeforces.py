n=int(input())
for i in range(n):
    m=int(input())
    a,b=0,0
    A=[]
    B=[]
    
    l=list(map(int,input().split()))
    for j in range(1,m+1):
        
        if(j%2!=0):
            jj=0
            for k in range(len(l)):
                if(l[k]%2==0):
                    jj=1
                    break
                else:
                    continue
            if(jj==1):
                for kk in range(len(l)):
                    if(l[kk]%2==0):
                        a=a+l[kk]
                        l.remove(l[kk])
                        break
                    else:
                        continue
            else:
                l.remove(l[0])
                break
                
                
        else:
            pp=0
            for k1 in range(len(l)):
                if(l[k1]%2!=0):
                    pp=1
                else:
                    continue
            if(pp==1):
                for k2 in range(len(l)):
                    if(l[k2]%2==0):
                        b=b+l[k2]
                        l.remove(l[k2])
                        
                        break
                    else:
                        continue
            else:
                l.remove(l[0])
                break
            
    if(a>b):
        print("ALICE")
    elif(a==b):
        print("TIE")
    else:
        print("BOB")
    A.clear()
    B.clear()
