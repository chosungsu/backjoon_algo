# N, M 읽기
N, M = map(int, input().split())
# N줄만큼의 문자열을 set에 저장시키기
s = set([input() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = input()
    if t in s:
        cnt += 1
print(cnt)