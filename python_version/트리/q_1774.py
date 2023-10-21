import sys

#-- inputs --#
input = sys.stdin.readline
n,m = map(int,input().split())
pos = [()]
for _ in range(n):
    x,y=map(int,input().split())
    pos.append((x,y))
# 이미 연결된 간선
cnt = n-1
parents = [i for i in range(n+1)]

#-- algo --#
def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

def get_dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#-- result --#
for _ in range(m):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)
        cnt -= 1
        
# 간선 생성
edges = []
for i in range(1,len(pos)):
    for j in range(i+1,len(pos)):
        if i == j:
            continue
        x1,y1 = pos[i]
        x2,y2 = pos[j]
        edges.append((get_dist(x1,y1,x2,y2),i,j))
edges.sort(reverse = True)

# 크루스칼
ans = 0
while cnt>0:
    w,a,b = edges.pop()
    if find(a) == find(b):
        continue
    cnt -= 1
    union(a,b)
    ans += w

print("%.2f" %ans)