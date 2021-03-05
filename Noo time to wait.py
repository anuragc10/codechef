n,h,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
if(x+A[0]>=h):
    print("YES")
else:
    print("NO")
