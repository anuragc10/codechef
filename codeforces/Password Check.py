s=input()
l=list(s)
l1=["!", "?", ".", ",", "_"]
ch=0
lo=0
d=0
up=0

if(len(l)>=5):
    for i in range(0,len(l)):
        if(l[i]>='A' and l[i]<='Z'):
            lo=lo+1
            break
    for i in range(0,len(l)):
        if(l[i]>='a' and l[i]<='z'):
            up=up+1
            break
    for i in range(0,len(l)):
        if(l[i].isdigit()):
            d=d+1
            break
    if(up>0 and lo>0 and d>0):
        print("Correct")
    else:
        print("Too weak")
else:
    print("Too weak")
