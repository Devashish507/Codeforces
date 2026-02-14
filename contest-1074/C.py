t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(set(arr))  # remove duplicates
    best = 1
    curr = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            curr += 1
        else:
            curr = 1
        best = max(best, curr)

    print(best)
