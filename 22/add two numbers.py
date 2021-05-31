s=input()
s=s[1:len(s)-1]
l1=list(s.split(","))

s2=input()
s2=s2[1:len(s2)-1]
l2=list(s2.split(","))


l1.reverse()
l2.reverse()

p1=""
p2=""
p1=p1.join(l1)
p2=p2.join(l2)

a=int(p1)+int(p2)
q=str(a)
l3=list(q)
l3.reverse()

st="["
for i in range(len(l3)):
    st=st+l3[i]+","
st=st+"]"
print(st[:len(st)-2] + st[len(st)-1:])
    
    
