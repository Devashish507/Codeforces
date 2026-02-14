t = int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    arr = list(map(int,input().split()))
    mapi = {
        -1:arr[:]
    }
    for q in range(m):
        b,c = map(int,input().split())
        isvalid = mapi[q-1][b-1]+c
        if isvalid <= h:
            mapi[q] = mapi[q-1][:]
            mapi[q][b-1] +=c 
        else:
            mapi[q] = arr[:]
    print(*mapi[m-1])           
        