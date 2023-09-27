import sys

input = sys.stdin.readline
N = int(input())

# 소수 문제에서는 미리 소수를 처리해놓는 것이 빠른 연산속도를 가져온다.(0,1 제외)
a = [False, False] + [True] * (N-1)
res = []

for i in range(2, N+1):
    # a[i]가 True로 설정되었을 때
    if a[i]:
        res.append(i)
        # i를 이용하여 소수가 아닌 a 내부를 False로 처리해준다. 마찬가지로 연산속도를 빠르게 가져오기 위함이다.
        for j in range(2*i, N+1, i):
            a[j] = False

answer = 0
start = 0
end = 0

# 소수만 담은 res의 길이보다 큰 end가 나오면 break
while end <= len(res):
    temp_sum = sum(res[start:end])
    # 주어진 수식인 N가 동일한 합인 경우
    if temp_sum == N:
        answer += 1
        end += 1
    # N보다 작은 합인 경우
    # 뒤 인덱스를 증가
    elif temp_sum < N:
        end += 1
    # N보다 큰 합인 경우
    # 앞 인덱스를 증가
    else:
        start += 1

print(answer)