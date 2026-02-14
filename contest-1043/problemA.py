t = int(input())
for _ in range(t):
    na = int(input())
    a = input()
    nb = int(input())
    b = input()
    c = input()
    for i in range(len(c)):
        if c[i]=='D':
            a+=b[i]
        else:
            a = b[i]+a
    print(a)            