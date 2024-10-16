def merge_sort(LIST):
    if len(LIST) == 1:
        return LIST
    #절반으로 나누어 합병정렬을 시도
    center = (len(LIST)+1) // 2
    Left= merge_sort(LIST[:center]);
    Right = merge_sort(LIST[center:]);
    i = 0
    j = 0
    tmp = []
    
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            tmp.append(Left[i])
            answer.append(Left[i])
            i += 1
        else:
            tmp.append(Right[j])
            answer.append(Right[j])
            j += 1
    
    while i < len(Left):
        tmp.append(Left[i])
        answer.append(Left[i])
        i += 1
    
    while j < len(Right):
        tmp.append(Right[j])
        answer.append(Right[j])
        j += 1
        
    return tmp
    
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
LIST = list(map(int, input().split()))
answer = []
merge_sort(LIST)
 
if len(answer) < K:
    print(-1)
else:
    print(answer[K-1])