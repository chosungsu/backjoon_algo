ls = sorted(list(map(int, input().split())))
# 정렬된 리스트 값 중에 마지막 가장 긴 변보다 두 변의 합이 더 큰 경우 그대로 출력
if ls[0] + ls[1] > ls[2]:
    print(sum(ls))
# 이외는 두 변의 두배에서 1을 뺀 값을 출력
else:
    print((ls[0] + ls[1]) * 2 - 1)