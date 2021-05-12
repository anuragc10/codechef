s=input()
l=list(s)
a=abs(ord('a')-ord(l[0]))
b=abs(26-a)
c=min(a,b)

for i in range(len(s)-1):
    z=abs(ord(l[i])-ord(l[i+1]))
    y=abs(26-z)
    c=c+min(z,y)

print(c)
