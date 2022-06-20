# 한 줄에서 연속적으로 스캐닝하는 파이썬 코드는 다음과 같다
# map(int, input().split()) : int형 변수를 공백기준으로 쪼개어 맵핑
H, M = map(int, input().split())
timer = int(input()) 

#아래줄 스캐닝 결과를 시간, 분으로 각각 플러스시키기
H += timer // 60
M += timer % 60

#분이 60이상일 경우 시간에 1플러스시키고 분은 60마이너스시키기
if M >= 60:
    H += 1
    M -= 60
#시간이 24시 이상일 경우 0시 이상으로 표시
if H >= 24:
    H -= 24

print(H,M)