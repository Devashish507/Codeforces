t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    odds = sorted(x for x in arr if x % 2 == 1)
    total = sum(arr)

    if not odds: 
        print(0)
    else:
        k = len(odds)
        exclude = sum(odds[: k // 2])
        print(total - exclude)
