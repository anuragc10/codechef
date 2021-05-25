s=input()
a=""
n=len(s)
i=0
while(i<n):
    if(s[i]=="."):
        a=a+"0"
    if(s[i]=="-" and s[i+1]=="."):
        i=i+1
        a=a+"1"
    if(s[i]=="-" and s[i+1]=="-"):
        i=i+1
        a=a+"2"
    i=i+1
print(a)
