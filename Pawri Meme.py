n=int(input())
for i in range(n):
    p=str(input())
    r='@@@@@'+p+'@@@@@'
    l=list(r)
    for j in range(len(l)):
        if(l[j]=='t' and l[j+1]=='y' and l[j-1]=='r' and l[j-2]=='a' and l[j-3]=='p'):
            l[j-1]='w'
            l[j]='r'
            l[j+1]='i'
            j=j+2
     
   

    q="".join(l)
    print(q[5:len(q)-5])
