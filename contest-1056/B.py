import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())

        # Known impossible case
        if n == 2 and k == 3:
            print("NO")
            continue

        print("YES")
        grid = [["L"] * n for _ in range(n)]  
        cnt = 0
        for i in range(n):
            for j in range(n):
                if cnt < k:
                    grid[i][j] = "U"
                    cnt += 1
                else:
                    a = i
                    b = j
                    break
                
                

        for row in grid:
            print("".join(row))

if __name__ == "__main__":
    solve()
