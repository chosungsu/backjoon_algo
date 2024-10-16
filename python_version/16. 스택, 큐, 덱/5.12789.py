N = int(input())
arr = list(map(int, input().split()))

# 대기줄 리스트로 초기화
stack = []
# 첫번째 순서이므로 1로 초기화
target = 1

# arr이 모두 비워질 때까지 반복됨.
while arr:
    # 간식을 받는 순서일 경우 주어진 리스트에서 pop
    # 더불어 순서를 1씩 증가
    if arr[0] == target:
        arr.pop(0)
        target += 1
    # 만약 해당 순서가 아니라면 대기줄로 추가시키기
    else:
        stack.append(arr.pop(0))
    # 마지막으로 대기줄에 존재하는 인원들을 차례로 보내게 된다.
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
 
if not stack: 
    print('Nice')
else:
    print('Sad')