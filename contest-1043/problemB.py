t = int(input())
for _ in range(t):
    n = int(input())
    xs = []
    p = 10  
    for k in range(1, 19):  
        d = 1 + p
        if d > n:
            break
        if n % d == 0:
            xs.append(n // d)
        p *= 10
    xs.sort()
    if not xs:
        print(0)
    else:
        print(len(xs), *xs)
