import heapq

#-- inputs --#
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
costMatrix = [[0] * n for _ in range(n)]
visited = [False] * n


#-- algo --#
def getDistance(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5

def findMST():
    pq = []
    heapq.heappush(pq, (0, 0))
    count = 0
    answer = 0
    while count < n:
        currDistance, start = heapq.heappop(pq)
        if not visited[start]:
            visited[start] = True
            answer += currDistance
            count += 1
            for i in range(n):
                dist = costMatrix[start][i]
                heapq.heappush(pq, (dist, i))
    return answer

#-- result --#
for i in range(n):
    for j in range(n):
        costMatrix[i][j] = getDistance(stars[i][0], stars[i][1], stars[j][0], stars[j][1])
print(round(findMST(),2))