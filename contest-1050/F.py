import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = input().strip()
    while line == "":
        line = input().strip()
    n = int(line)

    arrays = []
    maxlen = 0

    for _ in range(n):
        parts = list(map(int, input().split()))
        while len(parts) == 0:
            parts = list(map(int, input().split()))
        k = parts[0]
        arr_line = parts[1:]
        arrays.append(arr_line)
        if k > maxlen:
            maxlen = k

    if n == 1:
        print(*arrays[0])
        continue

    new_min = 0
    for i in range(1, n):
        if arrays[i][0] < arrays[new_min][0] or (arrays[i][0] == arrays[new_min][0] and arrays[i] < arrays[new_min]):
            new_min = i

    res = arrays[new_min].copy()

    while len(res) < maxlen:
        cur_pos = len(res)
        mini = 10**18
        candidate = -1
        for i, a in enumerate(arrays):
            if len(a) <= cur_pos:
                continue
            if a[cur_pos] < mini:
                mini = a[cur_pos]
                candidate = i
            elif a[cur_pos] == mini:
                if candidate == -1 or a[cur_pos:] < arrays[candidate][cur_pos:]:
                    candidate = i
        if candidate == -1:
            break
        res.extend(arrays[candidate][cur_pos:])

    print(*res)
