p=input()
s=""
q=""
for i in range(len(p)):
    s=s+p[i]
    q=q+p[i]
m1=-1
m2=-1

a=s.split("0")
r=q.split("1")

for i in range(len(a)):
    m1=max(m1,len(a[i]))
for j in range(len(r)):
    m2=max(m2,len(r[j]))
m=max(m1,m2)

if(m>=7):
    print("YES")
else:
    print("NO")
