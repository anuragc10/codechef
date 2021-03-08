import math
n=int(input())
def decimalToBinary(n): 
    return bin(n).replace("0b", "")
def binaryToDecimal(n): 
    return int(n,2)
for i in range(n):
    cbl=[]
    A=[]
    B=[]
    c=int(input())
    cb=list((decimalToBinary(c)))
    for i in cb:
        cbl.append(int(i))
        A.append(0)
        B.append(0)
    print(cbl,A,B)
    for i in range(len(cbl)):
        if(cbl[i]==0):
            A[i]=1
            B[i]=1
    print(cbl,A,B)
    for i in range(len(A)):
        if(A[i]==0):
            A[i]=1
            break
    print(cbl,A,B)
    for i in range(len(B)):
        if(A[i]==0):
            B[i]=1
    print(cbl,A,B)
    A = [str(i) for i in A]
    B = [str(i) for i in B]
    Ab = ("".join(A))
    Bb=("".join(B))
    print(Ab,Bb)
    Ad=binaryToDecimal(Ab)
    Bd=binaryToDecimal(Bb)
    print(Ad,Bd)

    print(Ad*Bd)
