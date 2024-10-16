import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# index, name별로 별도 딕셔너리 생성
dict = {}
for i in range(1, n + 1):
    poketmon = input().rstrip()
    dict[i] = poketmon
    dict[poketmon] = i
for _ in range(m):
    check = input().rstrip()
    # 숫자일 경우
    # 인덱스로부터 이름을 추출
    if check.isdigit():
        print(dict[int(check)])
    # 이름일 경우
    # 이름에서 인덱스 추출
    else:
        print(dict[check])