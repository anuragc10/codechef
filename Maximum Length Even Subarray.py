# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    m=(n*(n+1))/2
    if(m%2==0):
        print(n)
    else:
        print(n-1)
