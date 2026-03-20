n = int(input())

for i in range(n + 1):
    print("  " * (n - i), end="")
    
    row = list(range(i + 1)) + list(range(i - 1, -1, -1))
    print(" ".join(map(str, row)))

for i in range(n - 1, -1, -1):
    print("  " * (n - i), end="")
    
    row = list(range(i + 1)) + list(range(i - 1, -1, -1))
    print(" ".join(map(str, row)))