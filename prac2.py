deck =[17,13,11,2,3,5,7]
n = len(deck)
deck.sort()
result = [0] * n
positions = list(range(n))
idx = 0

for card in deck:
    result[positions[idx]] = card
    positions.pop(idx)
    if positions:
        idx = (idx + 1) % len(positions)

print(result)