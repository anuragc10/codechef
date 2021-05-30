s=input()
l=list(s)
n=len(s)
b=0
#a=s.lstrip("0")
#print(a)

a1=0
for i in range(n):
    if(l[i]!="0"):
        a1=i
        break
l1=l[a1:]
#print(a1)

for i in range(len(l1)):
    if(l1[i]=="0"):
        b=1
        del l1[i]
        break
if(b==0):
    for j in range(1,len(l1)):
        print(l1[j],end="")
else:
    for j in range(len(l1)):
        print(l1[j],end="")
