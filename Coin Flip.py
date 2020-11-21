n=int(input())

for _ in range(n):
    num=int(input())
    for p in range(num):
        q=list(map(int,input().split()))
        if(q[0]==1):
            if(q[1]%2==0):
                print(q[1]//2)
            else:
                if(q[2]==1):
                    print(q[1]//2)
                else:
                    print(q[1]//2 +1)
        else:
            if(q[1]%2==0):
                print(q[2]//2)
            else:
                if(q[2]==1):
                    print(q[2]//2 +1)
                else:
                    print(q[2]//2)
