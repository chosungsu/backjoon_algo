import sys

input = sys.stdin.readline
MAX = 1000000000

# 스택을 이용한 풀이
# 가장 큰 사각형의 넓이를 구하기 위해
# 스택에 쌓다가 직전 높이보다 낮은 값의 높이임을 파악하면 직전 높이를 pop한다
# 이어서 높은 높이는 push를 하게 되고 마지막 인덱스에서는 모두 pop을 진행한다.
# 마지막 줄에 0을 받게 되면 반복을 종료한다.
while True:
    box=  list(map(int, input().split()))
    if box[0] == 0:
        break
    stack = []
    res = 0
    for i, h in enumerate(box):
        # i == 0에는 갯수가 들어있어서 무시함.
        if i == 0:
            continue
        # 스택에 무언가 있으면서 직전 h보다 작은 h를 받게 된 경우(pop)
        if stack and stack[-1][1] > h:
            while stack:
                s_i, s_h = stack.pop()
                w = 1
                if stack:
                    w = stack[-1][0] + 1
                res = max((i - w) * s_h, res)
                # 현재 h보다 높은 stack값만 반영(이후 최대값 갱신 목적)
                if not stack or stack[-1][1] <= h:
                    break
        # 스택에 무언가 없는 무의 상태이거나 직전 h보다 큰 h를 받게 된 경우(push)
        if not stack or stack[-1][1] <= h:
            stack.append((i, h))
    while stack:
        s_i, s_h = stack.pop()
        w = 1
        if stack:
            w = stack[-1][0] + 1
        res = max((box[0] + 1 - w) * s_h, res)
    print(res)