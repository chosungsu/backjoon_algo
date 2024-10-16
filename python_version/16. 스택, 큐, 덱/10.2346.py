from collections import deque

N = int(input())
# index-key형태로 저장
q = deque(enumerate(map(int, input().split())))
arr = []

while q:
    # 우선 1번 풍선을 터뜨린다.
    idx, num = q.popleft()
    arr.append(idx + 1)
    
    # 다음 번호가 양수이면 우측이동, 음수이면 좌측이동
    if num > 0:
        q.rotate(-(num - 1))
    else:
        q.rotate(-num)
print(' '.join(map(str, arr)))