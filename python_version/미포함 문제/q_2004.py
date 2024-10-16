# 5가 몇번 나누어지는지를 구한다.
def fiveCount(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

# 2가 몇번 나누어지는지를 구한다.
def twoCount(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer


n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    # 2와 5의 개수를 nCm을 구할 때처럼 구해서 더 작은 개수를 선택한다.
    print(min(twoCount(n) - twoCount(m) - 
              twoCount(n - m), fiveCount(n) - 
              fiveCount(m) - fiveCount(n - m)))

