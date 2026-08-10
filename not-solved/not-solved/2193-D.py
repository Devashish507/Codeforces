import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    
    # prefix sum of b
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + b[i]
    
    ans = 0
    
    for i in range(n):
        x = a[i]
        
        # swords with strength >= x
        k = n - i
        
        # find max L such that prefix[L] <= k
        L = bisect.bisect_right(prefix, k) - 1
        
        ans = max(ans, x * L)
    
    print(ans)