n=int(input())
s=input()
l=list(s)
if(n==1 and l[0]=='0'):
    print(0)
else:
    a=[]
    y=l.count('0')
    a=['0']*y
    a.append('1')
    a.sort(reverse=True)    
    s=''
    print(s.join(a))
