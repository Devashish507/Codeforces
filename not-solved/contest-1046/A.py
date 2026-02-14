t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    second_half_diff = abs((c - a) - (d - b))
    
    if second_half_diff <= 2:
        print("YES")
    else:
        print("NO")
