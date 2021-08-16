t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    for c in range(1,n+1):
        for b in range(c,n+1,c):
            if(b%c==0):
                for a in range(c,n+1,b):
                    if(a%b==c):
                        count=count+1
    print(count)
