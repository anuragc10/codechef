t=int(input())
for _ in range(t):
    n=int(input())
    if(n>=2000):
        print("1")
    if(n>=1600 and n<2000):
        print("2")
    if(n<1600):
        print("3")
