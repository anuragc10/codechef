n=int(input())
l1=[]
l2=[]

alpha = 'a'
for i in range(0, 26): 
    l1.append(alpha) 
    alpha = chr(ord(alpha) + 1)
beta = 'A'
for i in range(0, 26): 
    l2.append(beta) 
    beta = chr(ord(beta) + 1)
l3=['0','1','2','3','4','5','6','7','8','9']
l4=['@','#','%','&','?']


for i in range(n):
    x1=False
    x2=False
    x3=False
    x4=False
    a=input()
    if(len(a)<10):
        print("NO")
    else:
        for j1 in range(len(a)):
            if(a[j1] in l1):
                x1=True
                break
        for j2 in range(len(a)):
            if(a[j2] in l2):
                x2=True
                break
        for j3 in range(len(a)):
            if(a[j3] in l3):
                x3=True
                break
        for j4 in range(len(a)):
            if(a[j4] in l4):
                x4=True
                break
        if(a[0] in l3):
            x3=False
        if(a[len(a)-1] in l3):
            x3=False
        if(a[0] in l4):
            x4=False
        if(a[len(a)-1] in l4):
            x4=False

        if(x1==True and x2==True and x3==True and x4==True):
            print("Yes")
        else:
            print("NO")
            
             
        
        
        
    
