n = input()

result = ""

for i in range(len(n)):
    digit = int(n[i])

    # Invert digit if beneficial
    if digit >= 5:
        inverted = 9 - digit
    else:
        inverted = digit

    # Leading digit cannot become 0
    if i == 0 and inverted == 0:
        result += n[i]
    else:
        result += str(inverted)

print(result)