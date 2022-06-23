import sys

K = int(sys.stdin.readline())

#동서남북 설명 : E=1, W=2, S=3, N=4
height = []
width = []
total = []
#동서쪽으로 움직이는 경우와 남북쪽으로 움직이는 경우를 나눠서 
#리스트에 넣어준다.
for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    # 동서
    if direction == 1 or direction ==2:
        height.append(length)
        total.append(length)
    # 남북
    else:
        width.append(length)
        total.append(length)

# 가장 큰 면적 구하기
bigbox = max(height) * max(width)

#세로 최대값 
maxhidx = total.index(max(height))
#가로최대값 
maxwidx = total.index(max(width))

#전체 이동에서 세로 최대값의 다음값에서 세로 최대값 이전의 가로값을 빼준것이 작은 사각형의 가로값 
small1 = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])
small2 = abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])

area = bigbox - (small1 * small2)
print(area*K)