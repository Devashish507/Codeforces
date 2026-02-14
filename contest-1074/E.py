import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    robots = set(map(int, input().split()))
    spikes = set(map(int, input().split()))
    dgdCode = input().strip()

    offset = 0
    alive = n

    for ch in dgdCode:
        if ch == 'L':
            offset -= 1
        else:
            offset += 1

        dead = []

        if len(robots) <= len(spikes):
            for r in robots:
                if r + offset in spikes:
                    dead.append(r)
        else:
            for s in spikes:
                x = s - offset
                if x in robots:
                    dead.append(x)

        for r in dead:
            robots.remove(r)

        alive -= len(dead)
        print(alive, end=" ")
    print()
