t=int(input())
for _ in range (t):
    n=int(input())
    a=0
    o=1
    while(n!=1):
        if(n%5==0):
            n=(4*n)//5
        elif(n%3==0):
            n=((2*n)//3)
        elif(n%2==0):
            n=(n//2)
        else:
            o=0
            break
        a=a+1
    if(o):
        print(a)
    else:
        print("-1")
