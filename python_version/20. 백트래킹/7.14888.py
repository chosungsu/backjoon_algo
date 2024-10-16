def dfs(depth, total):
    global maxi, mini, plus, minus, mul, div
    if depth == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if plus > 0:
        plus -= 1
        dfs(depth + 1, total + num[depth])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(depth + 1, total - num[depth])
        minus += 1
    if mul > 0:
        mul -= 1
        dfs(depth + 1, total * num[depth])
        mul += 1
    if div > 0:
        div -= 1
        dfs(depth + 1, int(total / num[depth]))
        div += 1

import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
maxi = -1e9
mini = 1e9
dfs(1, num[0])
print(maxi)
print(mini)