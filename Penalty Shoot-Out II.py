n=int(input())
for i in range(n):
    m=int(input())
    chanceA=m
    chanceB=m
    shotA=0
    shotB=0
    p=input()
    for j in range(2*m):
        if(j%2==0):
            shotA=shotA + int(p[j])
            chanceA-=1
        else:
            shotB=shotB + int(p[j])
            chanceB-=1

            
        if(shotA>shotB+chanceB):
            print(j+1)
            break
        elif shotB>shotA+chanceA:
            print(j+1)
            break
        elif shotA==shotB and j==2*m-1:
            print(j+1)
            break
            
