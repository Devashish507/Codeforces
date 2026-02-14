MOD = 10**9 + 7
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    MAX_POW = 31
    pow2 = [1] * (MAX_POW + 1)
    for i in range(1, MAX_POW + 1):
        pow2[i] = pow2[i-1] << 1
    P = [1] * (MAX_POW + 1)
    for L in range(1, MAX_POW + 1):
        P[L] = (L * pow(P[L-1], 2, MOD)) % MOD

    @lru_cache(None)
    def prefix_G(L, m):
        if m == 0:
            return 1
        if L == 0:
            return 1
        neededL = m.bit_length()
        if L > neededL:
            L = neededL
        if L == 0:
            return 1
        left_len = pow2[L-1] - 1
        if m <= left_len:
            return prefix_G(L-1, m)
        if m == left_len + 1:
            return (P[L-1] * (L % MOD)) % MOD
        take_right = m - (left_len + 1)
        res = (P[L-1] * (L % MOD)) % MOD
        res = (res * prefix_G(L-1, take_right)) % MOD
        return res

    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        a = [int(next(it)) for __ in range(n)]
        a.sort()
        ans = 1
        rem = k
        for val in a:
            if rem == 0:
                break
            L = val - 1
            if L <= MAX_POW:
                block_len = pow2[L]
            else:
                block_len = k + 1
            if rem >= block_len:
                ans = ans * (val % MOD) % MOD
                ans = ans * P[L] % MOD
                rem -= block_len
            else:
                if rem >= 1:
                    ans = ans * (val % MOD) % MOD
                    rem -= 1
                if rem > 0:
                    ans = ans * prefix_G(L, rem) % MOD
                    rem = 0
                break
        out.append(str(ans % MOD))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
