import bisect

t = int(input())

for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(n+m)
