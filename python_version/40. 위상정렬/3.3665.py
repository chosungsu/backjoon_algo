# 올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 
# 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.
# 올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. 
# (작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.
# 창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 
# 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 
# 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.
import sys
from collections import deque

input = sys.stdin.readline
T = int(input()) # 전체 개수

# 위상 정렬
def topologicalSort(n, graph, inDegree, isLinked):
    q = deque()
    res = []
    
    for team in range(1, n+1):
        if inDegree[team] == 0:
            q.append(team)
    
    while q:
        team = q.popleft()
        res.append(team)
        
        for adj_team in graph[team]:
            # 해당 간선이 실제로 연결되어 있는
            # 유효한 간선인지를 isLinked로 판단하여
            # 만약 0이라면 해당 간선은 무시
            if isLinked[team][adj_team] == 0:
                continue
            
            inDegree[adj_team] -= 1
            
            if inDegree[adj_team] == 0:
                q.append(adj_team)
    
    return res

for _ in range(T):
    n = int(input()) # 팀의 수
    rank_prev = list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)] # 실제 연결된 등수
    # isLinked[a][b]는 a -> b 간선이 실제로
    # 연결이 되어있는 실재하는 간선인지에 대한
    # boolean 값을 의미
    isLinked = [[0]*(n+1) for _ in range(n+1)]
    inDegree = [0]*(n+1) # 간선의 개수
    
    # 모든 단방향 간선을 통해
    # graph, isLinked와 inDegree 갱신
    for i in range(n-1):
        for j in range(i+1, n):
            team1 = rank_prev[i]
            team2 = rank_prev[j]
            
            graph[team1].append(team2)
            isLinked[team1][team2] = 1
            inDegree[team2] += 1
    
    m = int(input()) # 등수가 바뀐 쌍의 개수
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        if isLinked[a][b]: # a -> b가 이전 기록인 경우
            graph[b].append(a) # graph에서 a->b이었을텐데 이를 b->a로 갱신
            isLinked[a][b] = 0 # 기존 기록 삭제
            isLinked[b][a] = 1 # 새로 갱신
            inDegree[b] -= 1 # 기존 간선이 b방향이었지만 이를 삭제
            inDegree[a] += 1 # 새로 갱신
        elif isLinked[b][a]: # b -> a가 이전 기록인 경우
            graph[a].append(b) # graph에서 b->a이었을텐데 이를 a->b로 갱신
            isLinked[b][a] = 0 # 기존 기록 삭제
            isLinked[a][b] = 1 # 새로 갱신
            inDegree[a] -= 1 # 기존 간선이 a방향이었지만 이를 삭제
            inDegree[b] += 1 # 새로 갱신
    
    res = topologicalSort(n, graph, inDegree, isLinked)
    
    # 사이클이 존재하는 경우 순위를 확정지을 수 없으므로
    # IMPOSSIBLE 출력. 다만 유의할 점이 있는데,
    # 작년 순위가 1, 2, 3, 4로 주어졌다고 치고,
    # 상대적 변동이 2 3, 3 4로 주어졌다고 치면,
    # 1팀의 진입차수가 0이지만 그래프에는 2-3-4 사이클이
    # 존재하는 상태이다. 따라서 위상 정렬 내부에서는 1을
    # 현재 순위 리스트에 넣은 다음, 2 3 4 중에서 진입 차수
    # 가 0인 것이 없으므로 그대로 종료한다.
    # 즉 이 경우에는 사이클이 있더라도 res의 길이가 1이 되는
    # 케이스이므로, 이런 경우까지 고려하여 IMPOSSIBLE을 출력하는
    # 조건으로 len(res) < n을 작성해준 것이다.
    # 참고로, 문제에서 설명하는 "?"의 경우는 존재하지 않는다.
    # 이미 작년의 순위를 제공한 순간, 모든 노드 사이의 단방향
    # 간선이 존재하기 때문이다.
    if len(res) < n:
        print("IMPOSSIBLE")
    else:
        print(*res, sep=" ")
