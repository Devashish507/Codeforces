t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    total = sum((ai // x) * y for ai in a)
    
    ans = 0
    for ai in a:
        current = ai + (total - (ai // x) * y)
        ans = max(ans, current)
    
    print(ans)