d=input()
s=input()
s1="qwertyuiop"
l1=list(s1)
s2="asdfghjkl;"
l2=list(s2)
s3="zxcvbnm,./"
l3=list(s3)
st=""
if(d=="R"):
    for i in range(len(s)):
        if(s[i] in l1):
            c=l1.index(s[i])
            st=st+l1[c-1]
        if(s[i] in l2):
            c=l2.index(s[i])
            st=st+l2[c-1]
        if(s[i] in l3):
            c=l3.index(s[i])
            st=st+l3[c-1]
else:
    for i in range(len(s)):
        if(s[i] in l1):
            c=l1.index(s[i])
            st=st+l1[c+1]
        if(s[i] in l2):
            c=l2.index(s[i])
            st=st+l2[c+1]
        if(s[i] in l3):
            c=l3.index(s[i])
            st=st+l3[c+1]
print(st)
    
            
