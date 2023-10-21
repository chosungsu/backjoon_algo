import sys

#-- inputs --#
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0, people[i]] for i in range(N+1)] #[i][0]: 우수마을 x, [i][1]: 우수마을
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
#-- algo --#    
def village(start):
    visited[start] = True

    for i in tree[start]:
        if not visited[i]:
            village(i)
            dp[start][0] += max(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]
    
#-- result --#
village(1)
print(max(dp[1][0], dp[1][1]))