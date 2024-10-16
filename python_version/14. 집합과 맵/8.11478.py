import sys

S = list(sys.stdin.readline().rstrip())
res = set()

for j in range(1, len(S) + 1):
    for i in range(len(S)):
        res.add("".join(S[i : i + j]))

print(len(res))