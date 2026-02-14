import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    sets = []
    freq = [0] * (m + 1)
    element_to_sets = [[] for _ in range(m + 1)]

    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        sets.append(line[1:])
        for x in line[1:]:
            freq[x] += 1
            element_to_sets[x].append(i)

    for i in range(1, m + 1):
        if freq[i] == 0:
            print("NO")
            return

    def find_cover():
        covered = [False] * (m + 1)
        chosen = [False] * n
        covered_count = 0
        
        while covered_count < m:
            best_set_idx = -1
            max_new = -1
            for i in range(n):
                if not chosen[i]:
                    new_covered = 0
                    for x in sets[i]:
                        if not covered[x]:
                            new_covered += 1
                    if new_covered > max_new:
                        max_new = new_covered
                        best_set_idx = i
            
            if best_set_idx == -1:
                break
            
            chosen[best_set_idx] = True
            for x in sets[best_set_idx]:
                if not covered[x]:
                    covered[x] = True
                    covered_count += 1

        return chosen

    cover1 = find_cover()
    
    # Check for a second minimal cover
    for i in range(n):
        if cover1[i]:
            sets[i], sets[0] = sets[0], sets[i]
            
            cover2 = find_cover()
            
            is_same = True
            for j in range(n):
                if cover1[j] != cover2[j]:
                    is_same = False
                    break
            
            if not is_same:
                print("YES")
                return

            sets[i], sets[0] = sets[0], sets[i]

    print("NO")

t = int(sys.stdin.readline())
for _ in range(t):
    solve()