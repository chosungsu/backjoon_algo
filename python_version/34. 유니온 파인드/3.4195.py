import sys

#-- inputs --#
input=sys.stdin.readline
T=int(input())

#-- algo --#
def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        counter[a] += counter[b]

#-- result --#
for _ in range(T):
    F=int(input())
    parents = {}
    counter = {}
    for _ in range(F):
        name1, name2 = input().split()

        if name1 not in parents:
            parents[name1] = name1
            counter[name1] = 1
        if name2 not in parents:
            parents[name2] = name2
            counter[name2] = 1

        union(name1, name2)

        print(counter[find(name1)])