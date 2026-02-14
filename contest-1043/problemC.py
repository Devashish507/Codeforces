t = int(input())
for _ in range(t):
    n = int(input())
    cost = 0
    x = 0
    pow3 = 1 
    while n > 0:
        d = n % 3  
        c_x = ((x + 9) * pow3) // 3
        cost += d * c_x
        n //= 3
        x += 1
        pow3 *= 3
    print(cost)
