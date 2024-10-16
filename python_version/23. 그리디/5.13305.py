import sys

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split())) # N-1개
costs = list(map(int, input().split())) # N개

res = road[0] * costs[0]
fcosts = costs[0]
for i in range(1, N-1): # 마지막 지역의 코스트는 필요가 없어서 범위를 다음과 같이 설정
    if costs[i] < fcosts: # 각 지역의 코스트가 첫 코스트보다 작을 경우
        fcosts = costs[i]
    res += fcosts * road[i]
print(res)