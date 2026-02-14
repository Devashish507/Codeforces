t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = max(arr)
    print(k*n)