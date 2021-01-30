n=int(input())
for i in range(n):
    c=0
    p=0
   
    N,K=map(int,input().split())
    l=list(map(int,input().split()))
    if(l.count(-1)>(N//2)):
        print("Rejected")
        p=1
       
    elif(p!=1):
        for j in l:
            if(j>K):
                print("Too Slow")
                p=2
               
                break
    if(p==0):
        for k in l:
            if(k<=1 and k>=0):
                c=c+1
                
        if(c==len(l)):
            print("Bot")
        else:
            print("Accepted")
