N = int(input())

# 결국 제곱수에 해당하는 창문만 열려있게 된다.
def count_open_windows(N):
    return int(N ** 0.5)

result = count_open_windows(N)
print(result)
