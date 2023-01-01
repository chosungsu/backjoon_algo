T = int(input())
for _ in range(T):
    N = int(input())
    weardict = {}
    cnt = 1
    for _ in range(N):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]] += 1
        else:
            weardict[wear[1]] = 1
    for k in weardict.items():
        cnt *= (k[1]+1)
    print(cnt-1)