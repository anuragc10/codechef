n=input()
c=0
if(n[0]>'a' and n[0]<'h' and int(n[1])>1 and int(n[1])<8):
    c=8
else:
    if((n[0]=='a' or n[0]=='h') and (int(n[1])==1 or int(n[1])==8)):
        c=3
    else:
        c=5
print(c)
        
    
