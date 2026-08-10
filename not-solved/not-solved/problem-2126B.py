t = int(input())
for _ in range(t):
    n,k= map(int,input().split())
    s = list(map(int,input().split()))
    l=0
    r=0
    total = 0
    while r<len(s):
        if r-l+1 ==k:
            total+=1
            r+=2
            l=r
            continue
        if  s[r]==1:
            r+=1
            l=r
            continue
        else:
            r+=1
    print(total)                
    
