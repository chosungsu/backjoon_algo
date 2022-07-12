#1. 반복할 T를 읽기
T = int(input())
for i in range(T):
    #2. 종류 N개를 읽기
    N = int(input())
    #3. 딕셔너리에 담기
    weardict = {}
    for j in range(N):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]
    cnt = 1
    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)