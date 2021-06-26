n=int(input())
for i in range(n):
    l=[]
    s=input()
    for i in range(len(s)):
        l.append(s[i])
    if(l[0]=='1'):
        l.insert(1,'0')
    else:
        l.insert(0,'1')
    s=""
    print(s.join(l))
