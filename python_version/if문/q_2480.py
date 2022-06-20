# 한 줄에서 연속적으로 스캐닝하는 파이썬 코드는 다음과 같다
# map(int, input().split()) : int형 변수를 공백기준으로 쪼개어 맵핑
f, s, t = map(int, input().split())

if f == s == t:
    print(10000+f*1000)
elif f == s or f == t:
    print(1000+f*100)
elif s == t:
    print(1000+s*100)
else:
    print(100 * max(f,s,t))