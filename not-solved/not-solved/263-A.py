matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    
    if 1 in row:
        r = i + 1              # row index (1-based)
        c = row.index(1) + 1  # column index (1-based)

# Calculate moves
moves = abs(r - 3) + abs(c - 3)

print(moves)