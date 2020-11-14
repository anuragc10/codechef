n=int(input())
for i in range(n):
    s=input()
    p=len(s)
    q=p//2
    r=q+1
    
    if(len(s)%2==0):
        if(sorted(s[0:q:1])==sorted(s[q:p:1])):
            print("YES")
        else:
            print("NO")
    else:
        if(sorted(s[0:q:1])==sorted(s[r:p:1])):
            print("YES")
        else:
            print("NO")
        
