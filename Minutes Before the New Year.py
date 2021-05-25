n=int(input())
for i in range(n):
    h,m=map(int,input().split())
    c=(23-h)*60 + (60-m)
    print(c)
