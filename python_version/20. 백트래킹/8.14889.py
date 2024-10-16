def cal_diff(team1, team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += graph[team1[i]][team1[j]]
            sum_team2 += graph[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)
def dfs(team1, count, N, start):
    global ans

    if count == N//2:
        team2 = []
        for i in range(N):
            if i not in team1:
                team2.append(i)

        local_diff = cal_diff(team1, team2)
        ans = min(ans, local_diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            dfs(team1, count+1, N, i+1)
            team1.remove(i)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = int(1e9)
dfs([], 0, N, 0)
print(ans)