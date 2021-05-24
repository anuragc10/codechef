n=int(input())
s=input()
c=0
d=0
for i in s:
    if(i=="-"):
        if(c>0):
            c=c-1
    else:
        c=c+1
print(c)
