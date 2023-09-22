N = int(input())
#Enter는 입장을 알리는 로그이다.
#그 이외 닉네임 중복을 제거하여 갯수를 구하라.
arr = set()
cnt = 0
input()

for i in range(N - 1):
    strs = input().rstrip()
    if strs != 'ENTER':
        # 동일 인물이어도 한번 사용으로 기록함.
        arr.add(strs)
    else:
        # 엔터 이후에 딕셔너리 초기화 이전 전체 기록을 cnt에 저장함.
        cnt += len(arr)
        arr.clear()
cnt += len(arr)
print(cnt)