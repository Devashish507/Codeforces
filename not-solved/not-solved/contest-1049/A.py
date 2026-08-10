t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    m = s.count('0')
    total = 0
    for i in range(len(s)):
        if s[i]=='1' and i<m:
            total+=1
    print(total)        
    