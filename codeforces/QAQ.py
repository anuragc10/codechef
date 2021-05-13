s=input()
n=len(s)
c=0
for i in range(n):
    for j in range(i):
        for k in range(j):
            if(s[i]+s[j]+s[k]=='QAQ'):
                c=c+1
print(c)
    
