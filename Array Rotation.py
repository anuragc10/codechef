n=int(input())
l=list(map(int,input().split()))
s1=sum(l)
q=int(input())
q1=list(map(str,input().split()))
for i in range(q):
    s1=s1*2
    print(s1%1000000007)
