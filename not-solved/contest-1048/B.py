def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        ovens = list(map(int, input().split()))
        
        ovens.sort()
        total_cakes = 0
        ovens_to_use = min(n, m)
        
        for i in range(ovens_to_use):
            total_cakes += ovens[n - 1 - i] * (m - i)
        
        print(total_cakes)


if __name__ == "__main__":
    solve()
