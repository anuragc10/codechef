k,r=map(int,input().split())
s=1

for i in range(1,10):
    if((i*k)%10==0 or (i*k)%10==r):
        print(i)
        break
