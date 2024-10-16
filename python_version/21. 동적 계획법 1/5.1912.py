N = int(input())
arr = list(map(int, input().split()))

#이전값과 현재값을 합한 값이 현재값보다 크면 교체해서 최대치를 판단한다.
for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] + arr[i])
    
print(max(arr))