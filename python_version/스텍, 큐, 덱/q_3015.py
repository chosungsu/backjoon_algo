import sys

input = sys.stdin.readline
n = int(input())
stack = [] # (키, cnt)로 append
result = 0

for _ in range(n):
    # 한 줄씩 읽어오기
    oasis = int(input())
    # 키 값 초기화
    cnt = 1
    # 스택에 아무 것도 존재하지 않고 마지막 값이 현재 키 값보다 작은 경우
    while stack and stack[-1][0] <= oasis:
        height, cnt = stack.pop()
        # 같은 경우는 cnt를 유지
        if height == oasis:
            result += cnt
            cnt += 1
        # 작은 경우는 cnt를 초기화
        elif height < oasis:
            result += cnt
            cnt = 1
    if stack:
        result += 1
    stack.append((oasis, cnt))
# 결과값 출력
print(result)