import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

stack = []
max_v = 0
for i in range(N):
    idx = i
    # 스택에 값이 존재하면 큰 값을 만날 때까지 pop
    while stack and stack[-1][1] > lst[i]:
        idx, height = stack.pop()
        # 현재 안덱스와 해당인덱스까지의 차이와 높이를 곱해서 최대 넓이를 탐색
        rst = (i - idx) * height
        max_v = max(max_v, rst)
    stack.append([idx, lst[i]])

# 전체가 동일한 높이일 경우를 추가적으로 고려
while stack:
    idx, height = stack.pop()
    rst = (N - idx) * height
    max_v = max(max_v, rst)

print(max_v)