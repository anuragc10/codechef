n,m=map(int,input().split())
a=0
for i in range(n):
    l=list(map(str,input().split()))
    if('M' in l or 'C' in l or 'Y' in l):
        a=1
        
if(a==0):
    print("#Black&White")
else:
    print("#Color")
