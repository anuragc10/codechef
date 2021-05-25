n=int(input())
for i in range(n):
    a=input()
    b=input()
    c=input()
    o=1
    for i in range(len(a)):
        if(a[i]!=c[i] and b[i]!=c[i]):
            o=0
            break
    if(o==1):
        print("Yes")
    else:
        print("No")
