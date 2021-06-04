n=int(input())
l=list(map(int,input().split()))
if(l[n-1]==0):
    print("UP")
elif(l[n-1]==15):
    print("DOWN")
else:
    if(n==1):
        print("-1")
    else:
        if(l[n-2]<l[n-1]):
            print("UP")
        else:
            print("DOWN")

        
