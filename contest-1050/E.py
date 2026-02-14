def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = [0] * (n + 1)
    ct = [0] * (n + 1)

    for num in a:
        cnt[num] += 1

    for i in range(n + 1):
        if cnt[i] % k != 0:
            print(0)
            return
        else:
            cnt[i] //= k

    res = 0
    l = 0

    for r in range(n):
        ct[a[r]] += 1

        while ct[a[r]] > cnt[a[r]]:
            ct[a[l]] -= 1
            l += 1

        res += (r - l + 1)

    print(res)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    tc = int(input())
    for _ in range(tc):
        solve()
