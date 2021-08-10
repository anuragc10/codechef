# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l.sort()
    if(l[0]==l[1] and l[1]==l[2] and l[2]==l[3]):
        print("0")
    elif((l[0]==l[1] and l[1]==l[2]) or (l[1]==l[2] and l[2]==l[3])):
        print("1")
    else:
        print("2")
        
