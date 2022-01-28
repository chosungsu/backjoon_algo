x = int(input())
for i in range(1, x+1):
    y, z = map(int, input().split())
    print(f'Case #{i}: {y+z}')