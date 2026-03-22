t = int(input())

for _ in range(t):
    k = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    
    alice_score = a1 + a2
    bob_score = b1 + b2
    
    alice_wins = (a1 > b1) + (a2 > b2)
    bob_wins = (b1 > a1) + (b2 > a2)
    
    possible = False
    
    for x in range(k + 1):
        for y in range(k + 1):
            if x == y:
                continue
            
            a_total = alice_score + x
            b_total = bob_score + y
            
            a_rounds = alice_wins + (x > y)
            b_rounds = bob_wins + (y > x)
            
            if b_total > a_total or (b_total == a_total and b_rounds > a_rounds):
                possible = True
                break
        if possible:
            break
    
    print("YES" if possible else "NO")