import sys
input = sys.stdin.readline

name = input().strip()
num = int(input())

#name의 l~r번째 사이에 알파가 몇 번 나오는지 구해야 한다.
#따라서 name을 l과 r 두 분류로 하여 이중 리스트를 알파벳 수(26)와 전체 문자열 길이만큼 초기화한다.
arr = [[0] * 26 for _ in range(len(name) + 1)]
#반복문을 통해 나머지 문자도 리스트에 저장
for i in range(1, len(name) + 1):
    for j in range(26):
        arr[i][j] = arr[i-1][j] + (ord(name[i-1]) - 97 == j)

for _ in range(num):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    print(arr[r + 1][ord(alpha) - 97] - arr[l][ord(alpha) - 97])