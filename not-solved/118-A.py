s = input()

vowels = "aoyeui"
result = ""

for ch in s:
    ch = ch.lower()
    if ch not in vowels:
        result += "." + ch

print(result)