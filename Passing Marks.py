t=int(input())
for _ in range(t):
    Am,Bm,Cm,T,A,B,C=map(int,input().split())
    if(A>=Am and B>=Bm and C>=Cm):
        if(A+B+C>=T):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
