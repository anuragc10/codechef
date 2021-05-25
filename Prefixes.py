n=int(input())
l=input()
a=[]
for k in range(len(l)):
    a.append(l[k])
    
s=""
ans=0
for i in range(0,n-1,2):
    if(a[i]=="a" and a[i+1]=="a"):
        ans=ans+1
        a[i]="b"
    elif(a[i]=="b" and a[i+1]=="b"):
        ans=ans+1
        a[i]="a"
print(ans)
s=""
print(s.join(a))
    
