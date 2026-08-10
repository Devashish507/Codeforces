t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if x<0 or y<0 or x==y or y==1:
        print(-1)
    else:
        if x>y:
            if x-1<=y:
                print(-1)
            else:
                print(3)
        else:
            print(2)        
            