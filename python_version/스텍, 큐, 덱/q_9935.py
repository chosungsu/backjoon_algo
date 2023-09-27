import sys

# 입력값 처리
strings = sys.stdin.readline().rstrip()
exp = sys.stdin.readline().rstrip()

# stack으로 문자열 폭발 구현
stack = []
ex_len = len(exp)

for i in range(len(strings)):
    stack.append(strings[i])
    if ''.join(stack[-ex_len:]) == exp:
        for _ in range(ex_len):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')