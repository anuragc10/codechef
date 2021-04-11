t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s=input()
    l=list(s)
    n=a+b
    for i in range((n//2)+1):
        if(l[i]!=l[n-i-1]):
            if(l[i]=='0' and l[n-i-1]=="?"):
                l[n-i-1]="0"
            if(l[i]=='1' and l[n-i-1]=="?"):
                l[n-i-1]="1"
            if(l[i]=='?'):
                l[i]=l[n-i-1]
        else:
            if(l[i]=="?"):
                if(l.count("0")<a):
                    l[i]="0"
                    l[n-i-1]="0"
                else:
                    l[i]="1"
                    l[n-i-1]="1"
            
    if(len(l)==1):
        if(a==1):
            l[0]="0"
        else:
            l[0]="1"

    s1=''.join(l)
    
    if(l.count("0")==a and l.count("1")==b and s1==s1[::-1]):
        print(s1)
    else:
        print("-1")
                    
            

        
    
    
    
    
