def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    count_ab = 0
    # Check every possible shift x for conveyor A relative to B
    for x in range(n):
        valid = True
        for m in range(n):
            if a[(x + m) % n] >= b[m]:
                valid = False
                break
        if valid:
            count_ab += 1

    count_bc = 0
    # Check every possible shift y for conveyor C relative to B
    for y in range(n):
        valid = True
        for m in range(n):
            if b[m] >= c[(y + m) % n]:
                valid = False
                break
        if valid:
            count_bc += 1

    # Total triplets (i, j, k)
    print(n * count_ab * count_bc)