import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    requirements = []
    for _ in range(n):
        requirements.append(list(map(int, sys.stdin.readline().split()))) 
    total_points = 0
    last_time = 0
    last_side = 0
    for a, b in requirements:
        delta_t = a - last_time
        delta_s = abs(b - last_side)
        if (delta_t % 2) == (delta_s % 2):
            total_points += delta_t
        else:
            total_points += delta_t - 1
        last_time = a
        last_side = b
    remaining_time = m - last_time
    total_points += remaining_time
    
    print(total_points)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

main()