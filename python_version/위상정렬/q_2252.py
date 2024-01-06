# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 
# 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 
# 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.
# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)] # 위상정렬인 리스트 삽입
inDegree = [0]*(N+1) # 간선의 개수
for i in range(M):
    A, B = map(int, input().split()) # 한 줄의 A, B쌍의 위상정렬
    graph[A].append(B)
    inDegree[B] += 1 # B에 대하여 간선 수 증가
for j in range(1, N+1): # 1이상의 수이므로 1부터 반복문 실행
    if inDegree[j] == 0:
        q.append(j)

ans = []
while q:
    s = q.popleft() # pop과 동시에 결과값에 차례대로 삽입
    ans.append(s)
    
    for adj_s in graph[s]: # 위상정렬된 리스트에서 pop 원소가 존재하는 간선인 경우
        inDegree[adj_s] -= 1 # 간선 수를 1씩 감소시킨다.(pop되었기 때문에 간선연결이 해제되었다고 이해하면 된다.)
        if inDegree[adj_s] == 0: # 감소된 간선 수를 다시한번 체크하여 q에 삽입 가능한지 살핀다.
            q.append(adj_s)

print(*ans, sep=" ")