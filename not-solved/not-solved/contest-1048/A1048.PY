t= int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a==b:
        print(0)
    elif a==1 or b==1 or a%b ==0 or b%a==0:
        print(1)
    else:
        print(2)