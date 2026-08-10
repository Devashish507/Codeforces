t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    min_steps = min(abs(s-arr[0]),abs(arr[-1]-s))
    min_steps+=abs(arr[-1]-arr[0])
    print(min_steps)
