t = int(input())
curr = 0
for _ in range(t):
    op = input()
    if op == "X++" or op == "++X":
        curr += 1
    else:
        curr -= 1
print(curr)   