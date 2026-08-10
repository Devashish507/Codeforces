import sys

def solve():
    # Using fast I/O for 10^4 test cases
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        s = int(input_data[idx])
        k = int(input_data[idx+1])
        m = int(input_data[idx+2])
        idx += 3
        
        num_flips = m // k
        rem = m % k
        
        if num_flips == 0:
            sand_at_top = s
        elif k >= s:
            sand_at_top = s
        else:
            # Alternates between s and k when k < s
            if num_flips % 2 == 1:
                sand_at_top = k
            else:
                sand_at_top = s
        
        ans = max(0, sand_at_top - rem)
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()