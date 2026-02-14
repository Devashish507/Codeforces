
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    found = False
    for l in range(1, n-1):
        for r in range(l+1, n):
            s1 = sum(a[0:l]) % 3
            s2 = sum(a[l:r]) % 3
            s3 = sum(a[r:]) % 3
            
            if (s1 == s2 == s3) or (len(set([s1, s2, s3])) == 3):
                print(l, r)
                found = True
                break
        if found:
            break
    
    if not found:
        print(0, 0)
