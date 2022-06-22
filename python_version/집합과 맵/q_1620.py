from sys import stdin
def input():
    return stdin.readline().rstrip()
n, m = map(int, input().split())
# index, name별로 별도 딕셔너리 생성
by_id = {}
by_name = {}
for i in range(1, n + 1):
    poketmon = input()
    by_id[i] = poketmon
    by_name[poketmon] = i
for _ in range(m):
    x = input()
    # 숫자일 경우
    # 인덱스로부터 이름을 추출
    if x.isdigit():
        print(by_id[int(x)])
    # 이름일 경우
    # 이름에서 인덱스 추출
    else:
        print(by_name[x])