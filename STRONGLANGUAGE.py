t=int(input())
for i in range(t):
    n,K=map(int,input().split())
    s=str(input())
    q=K*'*'
    res = []
    curr, cnt = None, 0
    for chr in s:
      
        # increment for similar character
        if chr == curr:
            cnt += 1
        else:
            curr, cnt = chr, 1
          
        # if count exactly K, element is added
        if cnt == K:
            res.append(K * chr)
      
    # printing result
    if(q in res):
        print("Yes")
    else:
        print("No")
    
    
    
