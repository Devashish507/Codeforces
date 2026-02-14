powers = [1] * 17
for i in range(1, 17):
    powers[i] = powers[i-1] * 10

t = int(input())
for _ in range(t):
    k = int(input())

    d = 1
    total_prev = 0
    while k > 9 * powers[d-1] * d:
        group_digits = 9 * powers[d-1] * d
        k -= group_digits
        if d == 1:
            total_prev += 45
        else:
            total_prev += 45 * (d * powers[d-1] - (d-1) * powers[d-2])
        d += 1

    n = (k - 1) // d
    r = k - n * d
    start = powers[d-1]
    num = start + n

    def digit_sum(n):
        if n < 0:
            return 0
        s = 0
        m = 1
        while m <= n:
            q = n // (10 * m)
            r2 = n % (10 * m)
            d_val = r2 // m
            s += q * 45 * m
            s += d_val * (d_val - 1) // 2 * m
            s += (r2 % m + 1) * d_val
            m *= 10
        return s

    part1 = digit_sum(start + n - 1) - digit_sum(start - 1)
    num_str = str(num)
    part2 = sum(int(x) for x in num_str[:r])

    total_sum = total_prev + part1 + part2
    print(total_sum)
