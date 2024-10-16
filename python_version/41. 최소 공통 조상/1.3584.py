import sys

input=sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1) # 각 노드의 부모 노드

    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a # a가 b의 부모이므로 저장한다.

    # 구하려는 두 노드
    a, b = map(int, input().split())
    target_a = [a]
    target_b = [b]

    # 구하려는 두 노드의 부모 노드들을 반복문으로 저장
    while parent[a]:
        target_a.append(parent[a])
        a = parent[a]

    while parent[b]:
        target_b.append(parent[b])
        b = parent[b]

    # 두 노드의 루트 노드부터 확인하기 위해 레벨을 맞춘다.
    target_a_level = len(target_a) - 1
    target_b_level = len(target_b) - 1

    # 두 노드의 공통 조상을 찾는다.
    # 두 노드의 루트 노드가 다를 때까지 반복
    while target_a[target_a_level] == target_b[target_b_level]:
        target_a_level -= 1
        target_b_level -= 1

    # 이전 레벨의 노드가 공통 조상 노드
    print(target_a[target_a_level + 1])