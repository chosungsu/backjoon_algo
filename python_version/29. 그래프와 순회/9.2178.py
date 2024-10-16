import sys
from collections import deque

input = sys.stdin.readline
 
n,m = map(int,input().split())
array=[]
 
for i in range(n):
    array.append(list(map(int,input().strip())))
    
d = [[1,0],[0,1],[-1,0],[0,-1]]
 
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y1,x1 = queue.popleft()
        for dx,dy in d:
            if 0<=y1+dy<n and 0<=x1+dx<m:
                if array[y1+dy][x1+dx]==1:
                    array[y1+dy][x1+dx]=array[y1][x1]+1
                    queue.append((y1+dy,x1+dx))
 
 
bfs(0,0)
print(array[n-1][m-1])