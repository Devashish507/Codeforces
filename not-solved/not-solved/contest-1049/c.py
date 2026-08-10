import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    # Initial alternating sum
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]
    
    init = ans
    
    # First simple adjustment
    for i in range(n):
        ans = max(ans, init + i - (i % 2))
    
    # More complex logic with tracking minimums
    min_even = sys.maxsize // 2
    min_odd = sys.maxsize // 2
    
    for i in range(n):
        if i % 2 == 1:
            ans = max(ans, init + i + a[i] + a[i] - min_even)
            min_odd = min(min_odd, i - a[i] - a[i])
        else:
            ans = max(ans, init + i - a[i] - a[i] - min_odd)
            min_even = min(min_even, i + a[i] + a[i])
    
    print(ans)
