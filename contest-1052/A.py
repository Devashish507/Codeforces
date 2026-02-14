from collections import Counter

def helper(a):
    return a[1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 0:
        print(0)
        continue
    
    ct = Counter(arr)
    lis = [(num, freq) for num, freq in ct.items()]
    lis.sort(key=helper, reverse=True)
    
    maxi = lis[0][1] 
    count = 1
    
    for num, freq in lis[1:]:
        count += 1
        maxi = max(maxi, count * freq) 
    
    print(maxi)
