t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    coins = 0
    power = 1  # 2^0
    for i in range(n - 1, -1, -1):
        if arr[i] * power > c:
            coins += 1
        else:
            power *= 2  
    
    print(coins)
