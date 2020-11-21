n=int(input())
for i in range(n):
    act,nat=map(str,input().split())
    laddu=0
    for j in range(int(act)):
        acti=list(map(str,input().split()))
        if(len(acti)==2):
            if acti[0]=="CONTEST_WON":
                rank=int(acti[1])
                if rank<=20:
                    laddu+=(300+ 20 - rank)
                else:
                    laddu+=300
            elif acti[0]=="BUG_FOUND":
                severity = int(acti[1])
                laddu += severity
        else:
            if acti[0]=="TOP_CONTRIBUTOR":
                laddu+=300
            elif acti[0]=="CONTEST_HOSTED":
                laddu+=50
                acti.clear()


    if nat=="INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)
