board = [list(map(int, input().split())) for _ in range(9)]
max = -1
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if board[i][j] > max :
            max = board[i][j]
            x = i + 1
            y = j + 1
print(max)
print(x, y)