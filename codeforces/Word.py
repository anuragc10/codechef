s=input()
l=0
u=0
for i in s:
    if(i>='a' and i<='z'):
        l=l+1
    else:
        u=u+1
if(l>=u):
    print(s.lower())
else:
    print(s.upper())

    
